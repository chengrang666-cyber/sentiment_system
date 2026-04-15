from fastapi import APIRouter, HTTPException
import sqlite3
import json
import uuid
from datetime import datetime
import threading
from utils.collector import CommentCollector

router = APIRouter()

# 存储任务状态
task_status = {}

# 获取支持的平台列表
@router.get("/platforms")
def get_platforms():
    return {"platforms": ["weibo", "douyin"]}

# 开始采集数据
@router.post("/start")
def start_collection(data: dict):
    try:
        platform = data.get("platform")
        keywords = data.get("keywords", [])
        start_date = data.get("start_date")
        end_date = data.get("end_date")
        limit = data.get("limit", 100)
        
        # 生成任务ID
        task_id = f"task_{uuid.uuid4().hex[:8]}"
        
        # 保存任务到数据库
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 插入任务记录
        cursor.execute('''
        INSERT INTO tasks (id, type, status, config)
        VALUES (?, ?, ?, ?)
        ''', (task_id, "collection", "started", json.dumps(data)))
        
        # 插入采集记录
        cursor.execute('''
        INSERT INTO collections (task_id, platform, keywords, start_date, end_date, collection_limit)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (task_id, platform, json.dumps(keywords), start_date, end_date, limit))
        
        conn.commit()
        conn.close()
        
        # 启动采集任务
        task_status[task_id] = "started"
        threading.Thread(target=collect_comments, args=(task_id, platform, keywords, start_date, end_date, limit)).start()
        
        return {"task_id": task_id, "status": "started"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 采集评论的异步函数
def collect_comments(task_id, platform, keywords, start_date, end_date, limit):
    try:
        collector = CommentCollector()
        comments = collector.collect_comments(platform, keywords, start_date, end_date, limit)
        
        # 保存评论到数据库
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 查询采集ID
        cursor.execute('''
        SELECT id FROM collections WHERE task_id = ?
        ''', (task_id,))
        collection_id = cursor.fetchone()[0]
        
        # 插入评论
        for comment in comments:
            cursor.execute('''
            INSERT INTO comments (collection_id, content, platform, created_at, user_id)
            VALUES (?, ?, ?, ?, ?)
            ''', (collection_id, comment["content"], comment["platform"], comment["created_at"], comment["user_id"]))
        
        # 更新采集数量
        cursor.execute('''
        UPDATE collections SET count = ? WHERE task_id = ?
        ''', (len(comments), task_id))
        
        # 更新任务状态
        cursor.execute('''
        UPDATE tasks SET status = ? WHERE id = ?
        ''', ("completed", task_id))
        
        conn.commit()
        conn.close()
        
        task_status[task_id] = "completed"
    except Exception as e:
        print(f"采集任务失败: {e}")
        task_status[task_id] = "failed"
        # 更新任务状态为失败
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        cursor.execute('''
        UPDATE tasks SET status = ? WHERE id = ?
        ''', ("failed", task_id))
        conn.commit()
        conn.close()

# 获取采集任务状态
@router.get("/status")
def get_collection_status(task_id: str):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 查询任务状态
        cursor.execute('''
        SELECT status FROM tasks WHERE id = ?
        ''', (task_id,))
        result = cursor.fetchone()
        
        if not result:
            raise HTTPException(status_code=404, detail="Task not found")
        
        status = result[0]
        
        # 查询采集数量
        cursor.execute('''
        SELECT count FROM collections WHERE task_id = ?
        ''', (task_id,))
        count_result = cursor.fetchone()
        count = count_result[0] if count_result else 0
        
        conn.close()
        
        return {"status": status, "count": count}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 获取采集的数据
@router.get("/data")
def get_collection_data(task_id: str, page: int = 1, page_size: int = 20):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 查询采集ID
        cursor.execute('''
        SELECT id FROM collections WHERE task_id = ?
        ''', (task_id,))
        collection_result = cursor.fetchone()
        
        if not collection_result:
            raise HTTPException(status_code=404, detail="Collection not found")
        
        collection_id = collection_result[0]
        
        # 查询总数据量
        cursor.execute('''
        SELECT COUNT(*) FROM comments WHERE collection_id = ?
        ''', (collection_id,))
        total = cursor.fetchone()[0]
        
        # 计算偏移量
        offset = (page - 1) * page_size
        
        # 查询数据
        cursor.execute('''
        SELECT id, content, platform, created_at FROM comments 
        WHERE collection_id = ? 
        LIMIT ? OFFSET ?
        ''', (collection_id, page_size, offset))
        comments = cursor.fetchall()
        
        # 格式化数据
        data = []
        for comment in comments:
            data.append({
                "id": comment[0],
                "content": comment[1],
                "platform": comment[2],
                "created_at": comment[3]
            })
        
        conn.close()
        
        return {
            "data": data,
            "total": total,
            "page": page,
            "page_size": page_size
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 导出采集数据
@router.post("/export")
def export_collection_data(data: dict):
    try:
        task_id = data.get("task_id")
        format = data.get("format", "csv")
        
        # 这里应该实现导出逻辑，这里只是模拟
        
        return {"url": f"/exports/{task_id}.{format}"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))