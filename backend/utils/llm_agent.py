import faiss
import numpy as np
from transformers import AutoTokenizer, AutoModel
import torch
import json

class LLMAgent:
    def __init__(self, model_name="gpt-3.5-turbo"):
        # 初始化向量存储
        self.index = faiss.IndexFlatL2(768)  # 假设使用768维向量
        self.documents = []
        
        # 初始化分词器和模型用于嵌入
        self.tokenizer = AutoTokenizer.from_pretrained("bert-base-chinese")
        self.embedding_model = AutoModel.from_pretrained("bert-base-chinese")
    
    def get_embedding(self, text):
        """获取文本的嵌入向量"""
        inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True, max_length=512)
        with torch.no_grad():
            outputs = self.embedding_model(**inputs)
        return outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    
    def add_document(self, text):
        """添加文档到向量存储"""
        embedding = self.get_embedding(text)
        self.index.add(np.array([embedding]))
        self.documents.append(text)
    
    def search_similar(self, query, k=5):
        """搜索相似文档"""
        embedding = self.get_embedding(query)
        distances, indices = self.index.search(np.array([embedding]), k)
        return [(self.documents[i], distances[0][j]) for j, i in enumerate(indices[0])]
    
    def analyze_sentiment(self, text):
        """分析文本情感"""
        # 简化实现，使用规则匹配
        positive_words = ["好", "棒", "优秀", "满意", "喜欢", "赞", "不错", "精彩", "完美", "开心"]
        negative_words = ["差", "糟糕", "垃圾", "失望", "讨厌", "烂", "差", "慢", "贵", "坑"]
        
        positive_count = sum(1 for word in positive_words if word in text)
        negative_count = sum(1 for word in negative_words if word in text)
        
        if positive_count > negative_count:
            sentiment = "正面"
            score = min(1.0, positive_count / (positive_count + negative_count))
        elif negative_count > positive_count:
            sentiment = "负面"
            score = min(1.0, negative_count / (positive_count + negative_count))
        else:
            sentiment = "中性"
            score = 0.5
        
        return {"sentiment": sentiment, "score": score}
    
    def extract_keywords(self, text):
        """提取文本关键词"""
        # 简化实现，使用常见关键词
        common_keywords = ["产品", "服务", "价格", "质量", "物流", "包装", "体验", "速度", "客服", "性价比"]
        keywords = [keyword for keyword in common_keywords if keyword in text]
        return {"keywords": keywords[:10]}
    
    def track_public_opinion(self, texts, time_range):
        """追踪舆情趋势"""
        # 收集所有文本
        all_text = " ".join(texts)
        
        # 分析情感分布
        sentiments = []
        for text in texts:
            sentiment = self.analyze_sentiment(text)
            sentiments.append(sentiment)
        
        # 计算情感分布
        positive = sum(1 for s in sentiments if s.get("sentiment") == "正面") / len(sentiments)
        negative = sum(1 for s in sentiments if s.get("sentiment") == "负面") / len(sentiments)
        neutral = sum(1 for s in sentiments if s.get("sentiment") == "中性") / len(sentiments)
        
        # 提取关键词
        keywords_result = self.extract_keywords(all_text)
        
        return {
            "sentiment_distribution": {
                "positive": positive,
                "negative": negative,
                "neutral": neutral
            },
            "keywords": keywords_result.get("keywords", [])
        }
    
    def process_comments(self, comments):
        """处理评论列表"""
        results = []
        for comment in comments:
            # 分析情感
            sentiment = self.analyze_sentiment(comment)
            # 提取关键词
            keywords = self.extract_keywords(comment)
            # 添加到向量存储
            self.add_document(comment)
            
            results.append({
                "content": comment,
                "sentiment": sentiment,
                "keywords": keywords
            })
        return results