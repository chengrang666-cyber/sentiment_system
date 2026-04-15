from fastapi import APIRouter, HTTPException
import sqlite3
import json
import uuid
from datetime import datetime, timedelta
import threading
from utils.llm_agent import LLMAgent

router = APIRouter()

# 存储任务状态
task_status = {}

# 情感分析
@router.post("/sentiment")
def sentiment_analysis(data: dict):
    try:
        data_ids = data.get("data_ids", [])
        
        # 生成任务ID
        task_id = f"task_{uuid.uuid4().hex[:8]}"
        
        # 保存任务到数据库
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 插入分析任务记录
        cursor.execute('''
        INSERT INTO tasks (id, type, status, config)
        VALUES (?, ?, ?, ?)
        ''', (task_id, "analysis", "started", json.dumps(data)))
        
        # 查询评论内容
        comments = []
        for data_id in data_ids:
            cursor.execute('''
            SELECT id, content FROM comments WHERE id = ?
            ''', (data_id,))
            comment_result = cursor.fetchone()
            if comment_result:
                comments.append({"id": comment_result[0], "content": comment_result[1]})
        
        conn.commit()
        conn.close()
        
        # 启动分析任务
        task_status[task_id] = "started"
        threading.Thread(target=analyze_sentiment, args=(task_id, comments)).start()
        
        # 这里返回模拟结果，实际应用中应该返回任务ID，让客户端轮询结果
        results = []
        for comment in comments:
            # 模拟情感分析
            sentiment = "positive" if "好" in comment["content"] else "negative" if "坏" in comment["content"] else "neutral"
            score = 0.8 if sentiment != "neutral" else 0.5
            results.append({
                "id": comment["id"],
                "content": comment["content"],
                "sentiment": sentiment,
                "score": score
            })
        
        return {"results": results}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 分析情感的异步函数
def analyze_sentiment(task_id, comments):
    try:
        agent = LLMAgent()
        results = []
        
        for comment in comments:
            # 分析情感
            sentiment_result = agent.analyze_sentiment(comment["content"])
            results.append({
                "id": comment["id"],
                "content": comment["content"],
                "sentiment": sentiment_result.get("sentiment", "neutral"),
                "score": sentiment_result.get("score", 0.5)
            })
        
        # 更新任务状态
        task_status[task_id] = "completed"
        # 这里可以将结果保存到数据库
    except Exception as e:
        print(f"情感分析任务失败: {e}")
        task_status[task_id] = "failed"

# 关键词提取
@router.post("/keywords")
def keyword_extraction(data: dict):
    try:
        data_ids = data.get("data_ids", [])
        
        # 生成任务ID
        task_id = f"task_{uuid.uuid4().hex[:8]}"
        
        # 保存任务到数据库
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 插入分析任务记录
        cursor.execute('''
        INSERT INTO tasks (id, type, status, config)
        VALUES (?, ?, ?, ?)
        ''', (task_id, "analysis", "started", json.dumps(data)))
        
        # 查询评论内容
        comments = []
        for data_id in data_ids:
            cursor.execute('''
            SELECT content FROM comments WHERE id = ?
            ''', (data_id,))
            comment_result = cursor.fetchone()
            if comment_result:
                comments.append(comment_result[0])
        
        conn.commit()
        conn.close()
        
        # 启动分析任务
        task_status[task_id] = "started"
        threading.Thread(target=extract_keywords, args=(task_id, comments)).start()
        
        # 这里返回模拟结果
        keywords = [
            {"word": "产品", "frequency": 10, "sentiment": "positive"},
            {"word": "服务", "frequency": 8, "sentiment": "positive"},
            {"word": "价格", "frequency": 6, "sentiment": "negative"},
            {"word": "质量", "frequency": 5, "sentiment": "positive"}
        ]
        
        return {"keywords": keywords}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 提取关键词的异步函数
def extract_keywords(task_id, comments):
    try:
        agent = LLMAgent()
        # 合并所有评论
        all_text = " ".join(comments)
        # 提取关键词
        keywords_result = agent.extract_keywords(all_text)
        
        # 更新任务状态
        task_status[task_id] = "completed"
        # 这里可以将结果保存到数据库
    except Exception as e:
        print(f"关键词提取任务失败: {e}")
        task_status[task_id] = "failed"

# 舆情趋势分析
@router.post("/trend")
def trend_analysis(data: dict):
    try:
        data_ids = data.get("data_ids", [])
        time_range = data.get("time_range", "day")
        
        # 生成任务ID
        task_id = f"task_{uuid.uuid4().hex[:8]}"
        
        # 保存任务到数据库
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 插入分析任务记录
        cursor.execute('''
        INSERT INTO tasks (id, type, status, config)
        VALUES (?, ?, ?, ?)
        ''', (task_id, "analysis", "started", json.dumps(data)))
        
        # 查询评论内容
        comments = []
        for data_id in data_ids:
            cursor.execute('''
            SELECT content FROM comments WHERE id = ?
            ''', (data_id,))
            comment_result = cursor.fetchone()
            if comment_result:
                comments.append(comment_result[0])
        
        conn.commit()
        conn.close()
        
        # 启动分析任务
        task_status[task_id] = "started"
        threading.Thread(target=track_trend, args=(task_id, comments, time_range)).start()
        
        # 这里返回模拟结果
        trends = []
        for i in range(7):
            date = (datetime.now() - timedelta(days=6-i)).strftime("%Y-%m-%d")
            trends.append({
                "date": date,
                "positive": 0.6 + i*0.02,
                "negative": 0.2 - i*0.01,
                "neutral": 0.2 - i*0.01
            })
        
        return {"trends": trends}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 追踪趋势的异步函数
def track_trend(task_id, comments, time_range):
    try:
        agent = LLMAgent()
        # 追踪舆情趋势
        result = agent.track_public_opinion(comments, time_range)
        
        # 更新任务状态
        task_status[task_id] = "completed"
        # 这里可以将结果保存到数据库
    except Exception as e:
        print(f"舆情趋势分析任务失败: {e}")
        task_status[task_id] = "failed"