from fastapi import APIRouter, HTTPException
import sqlite3
import json

router = APIRouter()

# 获取用户列表
@router.get("/users")
def get_users():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 查询所有用户
        cursor.execute('''
        SELECT id, username, role FROM users
        ''')
        users = cursor.fetchall()
        
        # 格式化数据
        user_list = []
        for user in users:
            user_list.append({
                "id": user[0],
                "username": user[1],
                "role": user[2]
            })
        
        conn.close()
        
        return {"users": user_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 创建用户
@router.post("/users")
def create_user(data: dict):
    try:
        username = data.get("username")
        password = data.get("password")
        role = data.get("role", "user")
        
        # 简单的密码哈希模拟
        password_hash = f"hashed_{password}"
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 插入用户
        cursor.execute('''
        INSERT INTO users (username, password_hash, role)
        VALUES (?, ?, ?)
        ''', (username, password_hash, role))
        
        user_id = cursor.lastrowid
        
        conn.commit()
        conn.close()
        
        return {
            "id": user_id,
            "username": username,
            "role": role
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 更新用户
@router.put("/users/{user_id}")
def update_user(user_id: int, data: dict):
    try:
        username = data.get("username")
        password = data.get("password")
        role = data.get("role")
        
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 检查用户是否存在
        cursor.execute('''
        SELECT id FROM users WHERE id = ?
        ''', (user_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="User not found")
        
        # 更新用户信息
        if password:
            password_hash = f"hashed_{password}"
            cursor.execute('''
            UPDATE users SET username = ?, password_hash = ?, role = ? WHERE id = ?
            ''', (username, password_hash, role, user_id))
        else:
            cursor.execute('''
            UPDATE users SET username = ?, role = ? WHERE id = ?
            ''', (username, role, user_id))
        
        conn.commit()
        conn.close()
        
        return {
            "id": user_id,
            "username": username,
            "role": role
        }
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 删除用户
@router.delete("/users/{user_id}")
def delete_user(user_id: int):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 检查用户是否存在
        cursor.execute('''
        SELECT id FROM users WHERE id = ?
        ''', (user_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="User not found")
        
        # 删除用户
        cursor.execute('''
        DELETE FROM users WHERE id = ?
        ''', (user_id,))
        
        conn.commit()
        conn.close()
        
        return {"status": "success"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 获取任务列表
@router.get("/tasks")
def get_tasks():
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 查询所有任务
        cursor.execute('''
        SELECT id, type, status, created_at FROM tasks
        ''')
        tasks = cursor.fetchall()
        
        # 格式化数据
        task_list = []
        for task in tasks:
            task_list.append({
                "id": task[0],
                "type": task[1],
                "status": task[2],
                "created_at": task[3]
            })
        
        conn.close()
        
        return {"tasks": task_list}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 获取任务详情
@router.get("/tasks/{task_id}")
def get_task_detail(task_id: str):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 查询任务
        cursor.execute('''
        SELECT id, type, status, config, created_at FROM tasks WHERE id = ?
        ''', (task_id,))
        task = cursor.fetchone()
        
        if not task:
            raise HTTPException(status_code=404, detail="Task not found")
        
        # 构建响应
        response = {
            "id": task[0],
            "type": task[1],
            "status": task[2],
            "created_at": task[3],
            "result": {}
        }
        
        # 如果是采集任务，添加采集结果
        if task[1] == "collection":
            cursor.execute('''
            SELECT count FROM collections WHERE task_id = ?
            ''', (task_id,))
            collection_result = cursor.fetchone()
            if collection_result:
                response["result"]["count"] = collection_result[0]
        
        conn.close()
        
        return response
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 删除任务
@router.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    try:
        conn = sqlite3.connect('database.db')
        cursor = conn.cursor()
        
        # 检查任务是否存在
        cursor.execute('''
        SELECT id FROM tasks WHERE id = ?
        ''', (task_id,))
        if not cursor.fetchone():
            raise HTTPException(status_code=404, detail="Task not found")
        
        # 删除任务
        cursor.execute('''
        DELETE FROM tasks WHERE id = ?
        ''', (task_id,))
        
        conn.commit()
        conn.close()
        
        return {"status": "success"}
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 获取系统配置
@router.get("/config")
def get_config():
    try:
        # 模拟系统配置
        config = {
            "model_name": "llama2",
            "api_key": "...",
            "max_tokens": 1000
        }
        
        return config
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# 更新系统配置
@router.put("/config")
def update_config(data: dict):
    try:
        # 模拟更新系统配置
        config = {
            "model_name": data.get("model_name", "llama2"),
            "api_key": data.get("api_key", "..."),
            "max_tokens": data.get("max_tokens", 1000)
        }
        
        return config
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))