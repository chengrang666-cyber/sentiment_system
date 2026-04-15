# SentimentAI 社交媒体评论情感分析系统

## 项目简介

SentimentAI 是一个基于大模型智能体的社交媒体评论情感分析系统，通过采集微博、抖音等平台的用户评论数据，结合 LangChain 框架搭建具备感知、规划、工具调用能力的大模型智能体，对评论文本进行情感极性识别与强度分析，并通过可视化界面展示情感分布、舆情趋势等结果。

## 系统架构

系统采用前后端分离架构，主要分为以下几个模块：

1. **数据采集层**：使用 Python 结合 Requests、Selenium 框架实现微博、抖音等平台的评论数据爬取。
2. **大模型智能体层**：基于 LangChain 框架搭建大模型智能体架构，实现情感分析、关键词提取、舆情追踪等核心功能。
3. **模型支撑层**：采用 Hugging Face Transformers 框架实现模型的加载、训练与推理。
4. **可视化与 Web 层**：后端采用 FastAPI 框架搭建接口服务，前端采用 Vue.js/ECharts 框架开发可视化界面。

## 项目结构

```
├── backend/             # 后端代码
│   ├── app/             # 应用代码
│   │   ├── api/          # API 路由
│   │   ├── agents/       # 大模型智能体
│   │   ├── data/         # 数据存储
│   │   ├── models/       # 模型定义
│   │   └── utils/        # 工具函数
│   ├── data/             # 数据文件
│   ├── main.py           # 主应用入口
│   └── requirements.txt  # 依赖文件
├── crawler/             # 爬虫代码
│   ├── weibo_crawler.py  # 微博爬虫
│   └── douyin_crawler.py # 抖音爬虫
├── frontend/            # 前端代码
│   ├── public/           # 静态资源
│   ├── src/              # 源代码
│   │   ├── assets/        # 资源文件
│   │   ├── components/    # 组件
│   │   ├── views/         # 页面
│   │   ├── router/        # 路由
│   │   └── store/         # 状态管理
│   ├── index.html        # 主 HTML
│   ├── package.json      # 前端依赖
│   └── vite.config.js    # Vite 配置
├── finetune/            # 模型微调代码
│   ├── scripts/          # 微调脚本
│   └── data/             # 微调数据
└── docs/                # 文档
```

## 安装与运行

### 后端安装

1. 进入后端目录：
   ```bash
   cd backend
   ```

2. 安装依赖：
   ```bash
   pip install -r requirements.txt
   ```

3. 启动后端服务：
   ```bash
   python -m uvicorn main:app --host 0.0.0.0 --port 8000
   ```

### 前端安装

1. 进入前端目录：
   ```bash
   cd frontend
   ```

2. 安装依赖：
   ```bash
   npm install
   ```

3. 启动前端服务：
   ```bash
   npm run dev
   ```

### 访问系统

- 前端：http://localhost:3000/
- 后端 API：http://localhost:8000/

## 功能模块

### 1. 数据采集模块

- **微博爬虫**：爬取微博平台的评论数据，支持关键词搜索。
- **抖音爬虫**：爬取抖音平台的评论数据，支持关键词搜索。
- **数据预处理**：对采集到的数据进行清洗、去重、分词等处理。

### 2. 大模型智能体分析模块

- **情感分析**：识别评论的情感极性（正面、负面、中性）和情感强度。
- **关键词提取**：从评论中提取高频关键词，分析主题词聚类。
- **舆情追踪**：基于时间维度分析情感趋势和关键词变化。

### 3. 可视化展示模块

- **实时舆情监控大屏**：展示统计数据、情感分布饼图、高频关键词云、舆情趋势折线图和最近评论。
- **任务管理**：创建、启动、暂停和查看数据采集任务。
- **评论浏览**：搜索和筛选评论，查看详细的情感分析结果。
- **AI对话**：与大模型智能体进行交互，获取分析结果和建议。

### 4. 后台管理模块

- **系统参数配置**：配置系统运行参数。
- **用户权限管理**：管理用户账号和权限。
- **数据管理**：管理采集的评论数据和分析结果。
- **分析任务管理**：管理情感分析任务的执行。

## 技术栈

- **后端**：Python、FastAPI、LangChain、Transformers
- **前端**：Vue.js、ECharts、Element Plus
- **数据采集**：Requests、Selenium、BeautifulSoup
- **数据处理**：Pandas、NumPy、Scikit-learn
- **模型**：Hugging Face Transformers、PEFT (LoRA)
- **存储**：MySQL、Redis

## 模型微调

### 完整微调流程

1. **准备基础底层环境**
   - 确保安装了最新的 NVIDIA 显卡驱动
   - 安装 CUDA Toolkit 11.8 或 12.1

2. **运行微调脚本**
   ```bash
   cd finetune/scripts
   python finetune_lora.py
   ```

   该脚本会自动执行以下步骤：
   - 安装 PyTorch (CUDA 12.1 版本)
   - 安装 modelscope 库
   - 克隆 LLaMA-Factory 仓库
   - 安装 LLaMA-Factory 及其依赖
   - 下载 Qwen2.5-7B-Instruct 模型
   - 配置情感分析数据集
   - 启动 LLaMA-Factory WebUI

3. **在 WebUI 中进行 LoRA 微调**
   - 在浏览器中访问 http://localhost:7860
   - 选择模型：Qwen2.5-7B-Instruct
   - 选择数据集：my_sentiment_dataset
   - 选择微调方法：LoRA
   - 配置微调参数（建议使用默认参数）
   - 点击 "开始训练"

4. **加载微调后的模型**
   - 微调完成后，模型会保存在 `LLaMA-Factory/saves` 目录
   - 在 `backend/app/agents/sentiment_agent.py` 中修改模型路径

### 数据集说明

微调数据集位于 `/workspace/finetune/data/finetune_dataset_async.jsonl`，包含以下格式的样本：

```json
{
  "instruction": "分析以下评论的情感极性（正面/负面/中性）和情感强度（0-1之间的数值）",
  "input": "这个产品非常好，服务也很周到",
  "output": "情感极性：正面，情感强度：0.9"
}
```


## 性能指标

- **准确率**：微调后模型的情感分析准确率达到 90% 以上
- **推理速度**：平均处理每条评论的时间小于 0.5 秒
- **系统响应时间**：页面加载时间小于 2 秒

## 注意事项

1. **爬虫使用**：请遵守各平台的 robots.txt 规则，避免过度爬取导致 IP 被封。
2. **模型选择**：默认使用 OpenAI API，可根据需要替换为其他开源模型。
3. **环境配置**：确保安装了所有必要的依赖包，特别是大模型相关的包。
4. **数据存储**：生产环境建议使用 MySQL 或 MongoDB 存储数据，本演示版本使用内存存储。

## 未来规划

1. **扩展平台支持**：增加对知乎、小红书等平台的支持。
2. **增强模型能力**：使用更大的模型和更多的训练数据，提升情感分析准确率。
3. **添加预测功能**：基于历史数据预测舆情发展趋势。
4. **优化系统性能**：使用分布式处理和缓存技术，提升系统处理能力。

## 联系方式

- 项目维护者：SentimentAI Team
- 邮箱：contact@sentimentai.com
-  GitHub：https://github.com/sentimentai/sentiment-analysis-system
