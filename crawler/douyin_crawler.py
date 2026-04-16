from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pandas as pd

class DouyinCrawler:
    def __init__(self):
        # 配置浏览器选项
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')  # 无头模式
        options.add_argument('--no-sandbox')
        options.add_argument('--disable-dev-shm-usage')
        options.add_argument('user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36')
        
        self.driver = webdriver.Chrome(options=options)
    
    def crawl_comments(self, keyword, pages=5):
        comments = []
        
        try:
            # 打开抖音搜索页面
            url = f'https://www.douyin.com/search/{keyword}'
            self.driver.get(url)
            
            # 等待页面加载
            time.sleep(5)
            
            # 滚动页面加载更多内容
            for _ in range(pages):
                # 滚动到底部
                self.driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                time.sleep(3)
                
                # 提取评论
                comment_elements = self.driver.find_elements(By.CSS_SELECTOR, '.comment-content')
                for element in comment_elements:
                    comment_text = element.text.strip()
                    if comment_text:
                        comments.append({
                            'content': comment_text,
                            'platform': '抖音',
                            'time': time.strftime('%Y-%m-%d %H:%M:%S')
                        })
        except Exception as e:
            print(f"爬取时出错: {e}")
        finally:
            self.driver.quit()
        
        return comments
    
    def save_comments(self, comments, filename):
        df = pd.DataFrame(comments)
        df.to_csv(filename, index=False, encoding='utf-8-sig')
        print(f"已保存{len(comments)}条评论到{filename}")


