import mysql.connector
import redis
import os
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# MySQL数据库连接
def get_mysql_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',  # 默认用户名
            password='',  # 默认密码
            database='sentiment_analysis'
        )
        return connection
    except Exception as e:
        print(f"MySQL连接失败: {e}")
        return None

# Redis连接
def get_redis_connection():
    try:
        redis_url = os.getenv('REDIS_URL', 'redis://localhost:6379/0')
        r = redis.from_url(redis_url)
        return r
    except Exception as e:
        print(f"Redis连接失败: {e}")
        return None
