from langchain.agents import AgentType, initialize_agent
from langchain.llms import HuggingFacePipeline
from langchain.tools import Tool
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
import os
import jieba
from collections import Counter

class SentimentAgent:
    def __init__(self, model_path=None):
        # 初始化本地微调的大模型
        if model_path is None:
            # 默认模型路径
            model_path = os.path.join(
                os.path.dirname(os.path.dirname(os.path.dirname(__file__))),
                "finetune",
                "LLaMA-Factory",
                "saves",
                "Qwen2.5-7B-Instruct",
                "lora"
            )
        
        # 如果模型路径不存在，使用模拟的方式（适用于演示环境）
        if not os.path.exists(model_path):
            print(f"警告：模型路径不存在：{model_path}")
            print("使用模拟的情感分析方式...")
            self.llm = None
        else:
            print(f"加载本地微调模型：{model_path}")
            # 加载模型和tokenizer
            tokenizer = AutoTokenizer.from_pretrained(model_path, trust_remote_code=True)
            model = AutoModelForCausalLM.from_pretrained(
                model_path,
                trust_remote_code=True,
                device_map="auto"
            )
            
            # 创建pipeline
            pipe = pipeline(
                "text-generation",
                model=model,
                tokenizer=tokenizer,
                max_new_tokens=256,
                temperature=0.3,
                top_p=0.9,
                repetition_penalty=1.1
            )
            
            # 使用HuggingFacePipeline
            self.llm = HuggingFacePipeline(pipeline=pipe)
        
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
        if self.llm is not None:
            self.agent = initialize_agent(
                tools=tools,
                llm=self.llm,
                agent=AgentType.CHAT_ZERO_SHOT_REACT_DESCRIPTION,
                verbose=True
            )
        else:
            self.agent = None
    
    def analyze_sentiment(self, text):
        """分析文本情感"""
        if self.llm is not None:
            prompt = PromptTemplate(
                input_variables=["text"],
                template="分析以下文本的情感：\n{text}\n\n请返回：\n1. 情感极性（正面/负面/中性）\n2. 情感强度（0-1之间的数值）"
            )
            chain = LLMChain(llm=self.llm, prompt=prompt)
            result = chain.run(text)
            
            # 解析结果
            sentiment = "neutral"
            score = 0.5
            
            if "正面" in result:
                sentiment = "positive"
                score = 0.8
            elif "负面" in result:
                sentiment = "negative"
                score = 0.2
            
            return {"sentiment": sentiment, "score": score}
        else:
            # 模拟情感分析
            positive_words = ["好", "棒", "优秀", "满意", "周到", "精美", "快"]
            negative_words = ["差", "烂", "糟糕", "不满", "太慢", "退款", "态度不好"]
            
            sentiment = "neutral"
            score = 0.5
            
            text_lower = text.lower()
            positive_count = sum(1 for word in positive_words if word in text)
            negative_count = sum(1 for word in negative_words if word in text)
            
            if positive_count > negative_count:
                sentiment = "positive"
                score = 0.6 + 0.3 * (positive_count / (positive_count + negative_count + 1))
            elif negative_count > positive_count:
                sentiment = "negative"
                score = 0.4 - 0.3 * (negative_count / (positive_count + negative_count + 1))
            
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
        if self.agent is not None:
            return self.agent.run(query)
        else:
            # 模拟智能体回复
            if "情感" in query or "情绪" in query:
                return "我是 SentimentAI 智能助手，我可以帮您分析评论的情感极性和情感强度。"
            elif "关键词" in query:
                return "我可以帮您从评论文本中提取高频关键词。"
            elif "趋势" in query or "舆情" in query:
                return "我可以基于时间维度分析情感趋势和关键词变化。"
            else:
                return "您好！我是 SentimentAI 智能助手，有什么可以帮助您的吗？我可以进行情感分析、关键词提取和舆情追踪。"

if __name__ == '__main__':
    agent = SentimentAgent()
    result = agent.run("分析以下评论的情感：这个产品质量很好，服务也很周到")
    print(result)
