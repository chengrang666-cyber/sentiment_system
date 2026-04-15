from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import sqlite3
import os

# 初始化数据库
@asynccontextmanager
async def lifespan(app: FastAPI):
    # 启动时创建数据库表
    create_tables()
    yield
    # 关闭时的清理工作
    pass

app = FastAPI(lifespan=lifespan)

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 在生产环境中应该设置具体的前端地址
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 创建数据库表
def create_tables():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()
    
    # 创建用户表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password_hash TEXT NOT NULL,
        role TEXT NOT NULL DEFAULT 'user',
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    ''')
    
    # 创建任务表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS tasks (
        id TEXT PRIMARY KEY,
        type TEXT NOT NULL,
        status TEXT NOT NULL DEFAULT 'pending',
        config TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        user_id INTEGER,
        FOREIGN KEY (user_id) REFERENCES users (id)
    )
    ''')
    
    # 创建采集表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS collections (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id TEXT NOT NULL,
        platform TEXT NOT NULL,
        keywords TEXT NOT NULL,
        start_date TIMESTAMP NOT NULL,
        end_date TIMESTAMP NOT NULL,
        collection_limit INTEGER NOT NULL,
        count INTEGER DEFAULT 0,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        FOREIGN KEY (task_id) REFERENCES tasks (id)
    )
    ''')
    
    # 创建评论表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        collection_id INTEGER NOT NULL,
        content TEXT NOT NULL,
        platform TEXT NOT NULL,
        created_at TIMESTAMP NOT NULL,
        user_id TEXT,
        FOREIGN KEY (collection_id) REFERENCES collections (id)
    )
    ''')
    
    # 创建分析表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS analyses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        task_id TEXT NOT NULL,
        collection_id INTEGER NOT NULL,
        type TEXT NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        completed_at TIMESTAMP,
        FOREIGN KEY (task_id) REFERENCES tasks (id),
        FOREIGN KEY (collection_id) REFERENCES collections (id)
    )
    ''')
    
    # 创建关键词表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS keywords (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        analysis_id INTEGER NOT NULL,
        word TEXT NOT NULL,
        frequency INTEGER NOT NULL,
        sentiment TEXT NOT NULL,
        FOREIGN KEY (analysis_id) REFERENCES analyses (id)
    )
    ''')
    
    # 创建趋势表
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS trends (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        analysis_id INTEGER NOT NULL,
        date TIMESTAMP NOT NULL,
        positive REAL NOT NULL,
        negative REAL NOT NULL,
        neutral REAL NOT NULL,
        FOREIGN KEY (analysis_id) REFERENCES analyses (id)
    )
    ''')
    
    # 创建索引
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_comments_collection_id ON comments (collection_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_analyses_collection_id ON analyses (collection_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_keywords_analysis_id ON keywords (analysis_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_trends_analysis_id ON trends (analysis_id)')
    
    # 插入默认管理员用户
    cursor.execute('''
    INSERT OR IGNORE INTO users (username, password_hash, role) 
    VALUES ('admin', '$2b$12$EixZaYVK1fsbw1ZfbX3OXePaWxn96p36WQoeG6Lruj3vjPGga31lW', 'admin')
    ''')
    
    conn.commit()
    conn.close()

# 根路由
@app.get("/")
def read_root():
    return {"message": "社交媒体评论情感分析系统 API"}

# 导入路由
from routes import collection, analysis, management

app.include_router(collection.router, prefix="/api/collection", tags=["collection"])
app.include_router(analysis.router, prefix="/api/analysis", tags=["analysis"])
app.include_router(management.router, prefix="/api/management", tags=["management"])

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)