import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
import re
import time
import json

class CommentCollector:
    def __init__(self):
        # 配置Selenium
        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        self.driver = webdriver.Chrome(options=chrome_options)
    
    def __del__(self):
        if hasattr(self, 'driver'):
            self.driver.quit()
    
    def collect_weibo_comments(self, keywords, start_date, end_date, limit=100):
        """采集微博评论"""
        comments = []
        # 模拟微博搜索
        for keyword in keywords:
            url = f"https://s.weibo.com/weibo?q={keyword}"
            self.driver.get(url)
            time.sleep(3)  # 等待页面加载
            
            # 模拟滚动加载更多内容
            for _ in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            
            # 解析页面
            soup = BeautifulSoup(self.driver.page_source, 'html.parser')
            # 模拟获取评论
            for i in range(min(limit // len(keywords), 10)):
                comment = {
                    "content": f"这是关于{keyword}的评论{i+1}，内容很好",
                    "platform": "weibo",
                    "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "user_id": f"user_{i+1}"
                }
                comments.append(comment)
        return comments
    
    def collect_douyin_comments(self, keywords, start_date, end_date, limit=100):
        """采集抖音评论"""
        comments = []
        # 模拟抖音搜索
        for keyword in keywords:
            url = f"https://www.douyin.com/search/{keyword}"
            self.driver.get(url)
            time.sleep(3)  # 等待页面加载
            
            # 模拟滚动加载更多内容
            for _ in range(3):
                self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                time.sleep(2)
            
            # 模拟获取评论
            for i in range(min(limit // len(keywords), 10)):
                comment = {
                    "content": f"这是关于{keyword}的抖音评论{i+1}，内容不错",
                    "platform": "douyin",
                    "created_at": time.strftime("%Y-%m-%d %H:%M:%S"),
                    "user_id": f"user_{i+1}"
                }
                comments.append(comment)
        return comments
    
    def collect_comments(self, platform, keywords, start_date, end_date, limit=100):
        """根据平台采集评论"""
        if platform == "weibo":
            return self.collect_weibo_comments(keywords, start_date, end_date, limit)
        elif platform == "douyin":
            return self.collect_douyin_comments(keywords, start_date, end_date, limit)
        else:
            return []
    
    def clean_comment(self, content):
        """清洗评论内容"""
        # 去除多余的空白字符
        content = re.sub(r'\s+', ' ', content)
        # 去除表情符号
        content = re.sub(r'[\uD800-\uDBFF][\uDC00-\uDFFF]', '', content)
        # 去除特殊字符
        content = re.sub(r'[<>/{}()[]|\^~$%&*!@#$%^&*()_+=-]', '', content)
        return content.strip()