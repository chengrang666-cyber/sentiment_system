import requests
import re
from bs4 import BeautifulSoup
import pandas as pd
import time

class WeiboCrawler:
    def __init__(self):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
    
    def crawl_comments(self, keyword, pages=5):
        comments = []
        for page in range(1, pages + 1):
            url = f'https://s.weibo.com/weibo?q={keyword}&page={page}'
            try:
                response = requests.get(url, headers=self.headers)
                response.raise_for_status()
                soup = BeautifulSoup(response.text, 'lxml')
                
                # 提取评论内容
                comment_elements = soup.select('.content')
                for element in comment_elements:
                    comment_text = element.get_text(strip=True)
                    if comment_text:
                        comments.append({
                            'content': comment_text,
                            'platform': '微博',
                            'time': time.strftime('%Y-%m-%d %H:%M:%S')
                        })
                
                time.sleep(2)  # 避免请求过于频繁
            except Exception as e:
                print(f"爬取第{page}页时出错: {e}")
        
        return comments
    
    def save_comments(self, comments, filename):
        df = pd.DataFrame(comments)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"已保存{len(comments)}条评论到{filename}")


