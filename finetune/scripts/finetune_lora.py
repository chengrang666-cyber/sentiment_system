#!/usr/bin/env python3
"""
LLaMA-Factory LoRA 微调脚本
"""

import os
import subprocess
import sys

# 安装依赖
def install_dependencies():
    print("安装依赖...")
    # 安装 PyTorch (CUDA 12.1)
    subprocess.run([
        sys.executable, "-m", "pip", "install", 
        "torch", "torchvision", "torchaudio",
        "--index-url", "https://download.pytorch.org/whl/cu121"
    ], check=True)
    
    # 安装 modelscope
    subprocess.run([
        sys.executable, "-m", "pip", "install", "modelscope"
    ], check=True)

# 克隆 LLaMA-Factory
def clone_llama_factory():
    print("克隆 LLaMA-Factory 仓库...")
    if not os.path.exists("/workspace/finetune/LLaMA-Factory"):
        subprocess.run([
            "git", "clone", "https://github.com/hiyouga/LLaMA-Factory.git",
            "/workspace/finetune/LLaMA-Factory"
        ], check=True)
    else:
        print("LLaMA-Factory 已存在，跳过克隆")

# 安装 LLaMA-Factory
def install_llama_factory():
    print("安装 LLaMA-Factory 及其依赖...")
    subprocess.run([
        sys.executable, "-m", "pip", "install", "-e", ".[metrics]"
    ], cwd="/workspace/finetune/LLaMA-Factory", check=True)

# 下载模型
def download_model():
    print("下载 Qwen2.5-7B-Instruct 模型...")
    script = """
from modelscope import snapshot_download
model_dir = snapshot_download('qwen/Qwen2.5-7B-Instruct', cache_dir='./models')
print(f"模型已下载至: {model_dir}")
"""
    with open("/workspace/finetune/LLaMA-Factory/download_model.py", "w") as f:
        f.write(script)
    
    subprocess.run([
        sys.executable, "download_model.py"
    ], cwd="/workspace/finetune/LLaMA-Factory", check=True)

# 配置数据集
def configure_dataset():
    print("配置数据集...")
    # 复制数据集文件
    subprocess.run([
        "cp", "/workspace/finetune/data/finetune_dataset_async.jsonl",
        "/workspace/finetune/LLaMA-Factory/data/"
    ], check=True)
    
    # 配置 dataset_info.json
    dataset_info = '''{
  "my_sentiment_dataset": {
    "file_name": "finetune_dataset_async.jsonl",
    "columns": {
      "prompt": "instruction",
      "query": "input",
      "response": "output"
    }
  }
}
'''
    with open("/workspace/finetune/LLaMA-Factory/data/dataset_info.json", "w") as f:
        f.write(dataset_info)

# 启动 WebUI
def start_webui():
    print("启动 LLaMA-Factory WebUI...")
    print("请在浏览器中访问 http://localhost:7860")
    subprocess.run([
        "llamafactory-cli", "webui"
    ], cwd="/workspace/finetune/LLaMA-Factory")

if __name__ == "__main__":
    try:
        install_dependencies()
        clone_llama_factory()
        install_llama_factory()
        download_model()
        configure_dataset()
        start_webui()
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)
