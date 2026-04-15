from langchain.agents import AgentType, initialize_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
import re
import jieba
from collections import Counter

class SentimentAgent:
    def __init__(self):
        # 初始化LLM
        # 注意：这里使用OpenAI的API，实际项目中可以替换为其他开源模型
        self.llm = ChatOpenAI(temperature=0.3)
        
        # 定义工具
        tools = [
            Tool(
                name="情感分析",
                func=self.analyze_sentiment,
                description="分析文本的情感极性（正面、负面、中性）和情感强度"
            ),
            Tool(
                name="关键词提取",
                func=self.extract_keywords,
                description="从文本中提取高频关键词"
            ),
            Tool(
                name="舆情追踪",
                func=self.track_public_opinion,
                description="基于时间维度分析情感趋势和关键词变化"
            )
        ]
        
        # 初始化智能体
        self.agent = initialize_agent(
            tools=tools,
            llm=self.llm,
            agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )
    
    def analyze_sentiment(self, text):
        """分析文本情感"""
        prompt = PromptTemplate(
            input_variables=["text"],
            template="分析以下文本的情感：\n{text}\n\n请返回：\n1. 情感极性（正面/负面/中性）\n2. 情感强度（0-1之间的数值）"
        )
        chain = LLMChain(llm=self.llm, prompt=prompt)
        result = chain.run(text)
        
        # 解析结果
        sentiment = "中性"
        score = 0.5
        
        if "正面" in result:
            sentiment = "positive"
            score = 0.8
        elif "负面" in result:
            sentiment = "negative"
            score = 0.2
        
        return {"sentiment": sentiment, "score": score}
    
    def extract_keywords(self, text):
        """提取关键词"""
        # 使用jieba分词
        words = jieba.cut(text)
        # 过滤停用词
        stopwords = set(["的", "了", "和", "与", "或", "但", "是", "在", "有", "我"])
        filtered_words = [word for word in words if word not in stopwords and len(word) > 1]
        # 统计词频
        word_counts = Counter(filtered_words)
        # 返回前10个高频词
        top_keywords = word_counts.most_common(10)
        return {"keywords": [{'name': word, 'value': count} for word, count in top_keywords]}
    
    def track_public_opinion(self, data):
        """追踪舆情趋势"""
        # 模拟舆情追踪结果
        return {
            "trend": {
                "dates": ["12-26", "12-27", "12-28", "12-29", "12-30", "12-31", "01-01"],
                "positive": [120, 132, 101, 134, 90, 230, 210],
                "neutral": [220, 182, 191, 234, 290, 330, 310],
                "negative": [150, 232, 201, 154, 190, 330, 410]
            }
        }
    
    def run(self, query):
        """运行智能体"""
        return self.agent.run(query)

if __name__ == '__main__':
    agent = SentimentAgent()
    result = agent.run("分析以下评论的情感：这个产品质量很好，服务也很周到")
    print(result)
