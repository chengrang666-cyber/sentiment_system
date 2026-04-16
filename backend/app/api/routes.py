from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
import json
import os
from crawler.weibo_crawler import WeiboCrawler

router = APIRouter()

# 模拟数据
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

# 模拟任务数据
tasks = [
    {
        "id": 1,
        "keyword": "产品质量",
        "platform": "微博",
        "status": "completed",
        "collected_count": 5,
        "analyzed_count": 5
    }
]

# 模拟评论数据
comments = [
    {
        "id": 1,
        "content": "这个产品非常好，服务也很周到",
        "platform": "微博",
        "sentiment": "positive",
        "sentiment_score": 0.8,
        "time": "2023-01-01 12:00"
    },
    {
        "id": 2,
        "content": "价格有点贵，但是质量还可以",
        "platform": "微博",
        "sentiment": "neutral",
        "sentiment_score": 0.5,
        "time": "2023-01-02 10:30"
    }
]

# 模拟统计数据
stats = {
    "totalTasks": 1,
    "collectedComments": 5,
    "analyzedComments": 5,
    "averageSentiment": 3.2
}

@router.get("/tasks")
def get_tasks():
    return tasks

@router.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "keyword": task.keyword,
        "platform": task.platform,
        "status": "running",
        "collected_count": 0,
        "analyzed_count": 0
    }
    
    # 如果是微博平台，使用cookie调用爬虫
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
        
        # 更新任务状态和统计信息
        new_task["collected_count"] = len(comments_list)
        new_task["status"] = "completed"
    
    tasks.append(new_task)
    return new_task

@router.get("/comments")
def get_comments():
    return comments

@router.get("/stats")
def get_stats():
    return stats

@router.get("/sentiment/distribution")
def get_sentiment_distribution():
    return {
        "data": [
            {"value": 3, "name": "正面"},
            {"value": 1, "name": "中性"},
            {"value": 1, "name": "负面"}
        ]
    }

@router.get("/keywords")
def get_keywords():
    return {
        "data": [
            {"name": "产品", "value": 100},
            {"name": "服务", "value": 80},
            {"name": "质量", "value": 70},
            {"name": "价格", "value": 60},
            {"name": "体验", "value": 50},
            {"name": "物流", "value": 40},
            {"name": "客服", "value": 30},
            {"name": "包装", "value": 20}
        ]
    }

@router.get("/trend")
def get_trend():
    return {
        "data": {
            "dates": ["12-26", "12-27", "12-28", "12-29", "12-30", "12-31", "01-01"],
            "positive": [120, 132, 101, 134, 90, 230, 210],
            "neutral": [220, 182, 191, 234, 290, 330, 310],
            "negative": [150, 232, 201, 154, 190, 330, 410]
        }
    }
