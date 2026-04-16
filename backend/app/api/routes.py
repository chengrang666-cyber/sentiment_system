from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
import os
from crawler.weibo_crawler import WeiboCrawler
from app.database import get_mysql_connection, get_redis_connection

router = APIRouter()

# 数据模型
class TaskCreate(BaseModel):
    keyword: str
    platform: str
    start_date: str
    end_date: str

class Task(BaseModel):
    id: int
    keyword: str
    platform: str
    status: str
    collected_count: int
    analyzed_count: int

class Comment(BaseModel):
    id: int
    content: str
    platform: str
    sentiment: str
    sentiment_score: float
    time: str

@router.get("/tasks")
def get_tasks():
    connection = get_mysql_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="数据库连接失败")
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT id, keyword, platform, status, collected_count, analyzed_count 
            FROM tasks 
            ORDER BY created_at DESC
        """
        cursor.execute(query)
        tasks = cursor.fetchall()
        return tasks
    finally:
        if connection:
            connection.close()

@router.post("/tasks")
def create_task(task: TaskCreate):
    connection = get_mysql_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="数据库连接失败")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # 插入任务到数据库
        insert_task_query = """
            INSERT INTO tasks (user_id, keyword, platform, start_date, end_date, status)
            VALUES (%s, %s, %s, %s, %s, %s)
        """
        # 暂时使用用户ID为1（默认管理员）
        user_id = 1
        status = "running"
        
        cursor.execute(insert_task_query, (
            user_id, 
            task.keyword, 
            task.platform, 
            task.start_date, 
            task.end_date, 
            status
        ))
        
        # 获取新任务的ID
        task_id = cursor.lastrowid
        
        # 如果是微博平台，使用cookie调用爬虫
        collected_count = 0
        if task.platform == "微博":
            # 从环境变量获取微博cookie
            weibo_cookie = os.getenv("WEIBO_COOKIE")
            cookie_dict = {}
            
            # 解析cookie字符串为字典
            if weibo_cookie:
                cookie_pairs = weibo_cookie.split('; ')
                for pair in cookie_pairs:
                    if '=' in pair:
                        key, value = pair.split('=', 1)
                        cookie_dict[key] = value
            
            # 创建爬虫实例并爬取评论
            crawler = WeiboCrawler(cookie=cookie_dict)
            comments_list = crawler.crawl_comments(task.keyword, pages=3)
            
            # 插入评论到数据库
            for comment in comments_list:
                insert_comment_query = """
                    INSERT INTO comments (task_id, content, platform, publish_time)
                    VALUES (%s, %s, %s, %s)
                """
                cursor.execute(insert_comment_query, (
                    task_id, 
                    comment['content'], 
                    comment['platform'], 
                    comment['time']
                ))
            
            # 更新任务状态和统计信息
            collected_count = len(comments_list)
            status = "completed"
            update_task_query = """
                UPDATE tasks 
                SET status = %s, collected_count = %s 
                WHERE id = %s
            """
            cursor.execute(update_task_query, (status, collected_count, task_id))
        
        # 提交事务
        connection.commit()
        
        # 返回新任务信息
        return {
            "id": task_id,
            "keyword": task.keyword,
            "platform": task.platform,
            "status": status,
            "collected_count": collected_count,
            "analyzed_count": 0
        }
    finally:
        if connection:
            connection.close()

@router.get("/comments")
def get_comments():
    connection = get_mysql_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="数据库连接失败")
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT c.id, c.content, c.platform, 
                   COALESCE(a.sentiment, 'neutral') as sentiment, 
                   COALESCE(a.sentiment_score, 0) as sentiment_score, 
                   c.publish_time as time
            FROM comments c
            LEFT JOIN analysis_results a ON c.id = a.comment_id
            ORDER BY c.collected_at DESC
            LIMIT 100
        """
        cursor.execute(query)
        comments = cursor.fetchall()
        return comments
    finally:
        if connection:
            connection.close()

@router.get("/stats")
def get_stats():
    connection = get_mysql_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="数据库连接失败")
    
    try:
        cursor = connection.cursor(dictionary=True)
        
        # 获取总任务数
        cursor.execute("SELECT COUNT(*) as totalTasks FROM tasks")
        total_tasks = cursor.fetchone()['totalTasks']
        
        # 获取采集评论数
        cursor.execute("SELECT COUNT(*) as collectedComments FROM comments")
        collected_comments = cursor.fetchone()['collectedComments']
        
        # 获取已分析评论数
        cursor.execute("SELECT COUNT(*) as analyzedComments FROM analysis_results")
        analyzed_comments = cursor.fetchone()['analyzedComments']
        
        # 获取平均情感分
        cursor.execute("SELECT AVG(sentiment_score) as averageSentiment FROM analysis_results")
        avg_sentiment = cursor.fetchone()['averageSentiment'] or 0
        
        return {
            "totalTasks": total_tasks,
            "collectedComments": collected_comments,
            "analyzedComments": analyzed_comments,
            "averageSentiment": round(avg_sentiment, 1)
        }
    finally:
        if connection:
            connection.close()

@router.get("/sentiment/distribution")
def get_sentiment_distribution():
    connection = get_mysql_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="数据库连接失败")
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT 
                sentiment, 
                COUNT(*) as value 
            FROM analysis_results 
            GROUP BY sentiment
        """
        cursor.execute(query)
        results = cursor.fetchall()
        
        # 确保返回所有三种情感类型
        sentiment_map = {"positive": 0, "neutral": 0, "negative": 0}
        for result in results:
            sentiment_map[result['sentiment']] = result['value']
        
        data = [
            {"value": sentiment_map["positive"], "name": "正面"},
            {"value": sentiment_map["neutral"], "name": "中性"},
            {"value": sentiment_map["negative"], "name": "负面"}
        ]
        
        return {"data": data}
    finally:
        if connection:
            connection.close()

@router.get("/keywords")
def get_keywords():
    connection = get_mysql_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="数据库连接失败")
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT keyword as name, frequency as value 
            FROM keywords 
            ORDER BY frequency DESC 
            LIMIT 20
        """
        cursor.execute(query)
        data = cursor.fetchall()
        return {"data": data}
    finally:
        if connection:
            connection.close()

@router.get("/trend")
def get_trend():
    connection = get_mysql_connection()
    if not connection:
        raise HTTPException(status_code=500, detail="数据库连接失败")
    
    try:
        cursor = connection.cursor(dictionary=True)
        query = """
            SELECT 
                DATE_FORMAT(date, '%m-%d') as date_str, 
                positive_count, 
                neutral_count, 
                negative_count
            FROM sentiment_trends 
            ORDER BY date ASC 
            LIMIT 7
        """
        cursor.execute(query)
        results = cursor.fetchall()
        
        # 处理结果
        dates = []
        positive = []
        neutral = []
        negative = []
        
        for result in results:
            dates.append(result['date_str'])
            positive.append(result['positive_count'])
            neutral.append(result['neutral_count'])
            negative.append(result['negative_count'])
        
        # 如果没有数据，返回空数组
        if not dates:
            dates = []
            positive = []
            neutral = []
            negative = []
        
        return {
            "data": {
                "dates": dates,
                "positive": positive,
                "neutral": neutral,
                "negative": negative
            }
        }
    finally:
        if connection:
            connection.close()
