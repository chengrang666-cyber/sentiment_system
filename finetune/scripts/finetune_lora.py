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
    # 使用相对路径
    llama_factory_dir = os.path.join(os.path.dirname(os.path.dirname(__file__)), "LLaMA-Factory")
    
    # 检查目录是否存在且是有效的Python项目
    is_valid_project = os.path.exists(llama_factory_dir) and (
        os.path.exists(os.path.join(llama_factory_dir, "setup.py")) or 
        os.path.exists(os.path.join(llama_factory_dir, "pyproject.toml"))
    )
    
    if not is_valid_project:
        # 如果目录存在但不是有效项目，先删除
        if os.path.exists(llama_factory_dir):
            import shutil
            shutil.rmtree(llama_factory_dir)
            print("删除无效的 LLaMA-Factory 目录")
        
        # 重新克隆
        subprocess.run([
            "git", "clone", "https://github.com/hiyouga/LLaMA-Factory.git",
            llama_factory_dir
        ], check=True)
        print("LLaMA-Factory 仓库克隆成功")
    else:
        print("LLaMA-Factory 已存在且有效，跳过克隆")
    
    return llama_factory_dir

# 安装 LLaMA-Factory
def install_llama_factory(llama_factory_dir):
    print("安装 LLaMA-Factory 及其依赖...")
    subprocess.run([
        sys.executable, "-m", "pip", "install", "-e", ".[metrics]"
    ], cwd=llama_factory_dir, check=True)

# 下载模型
def download_model(llama_factory_dir):
    print("下载 Qwen2.5-7B-Instruct 模型...")
    script = """
from modelscope import snapshot_download
model_dir = snapshot_download('qwen/Qwen2.5-7B-Instruct', cache_dir='./models')
print(f"模型已下载至: {model_dir}")
"""
    download_script_path = os.path.join(llama_factory_dir, "download_model.py")
    with open(download_script_path, "w") as f:
        f.write(script)
    
    subprocess.run([
        sys.executable, "download_model.py"
    ], cwd=llama_factory_dir, check=True)

# 配置数据集
def configure_dataset(llama_factory_dir):
    print("配置数据集...")
    # 获取数据文件路径
    current_dir = os.path.dirname(os.path.dirname(__file__))
    dataset_file = os.path.join(current_dir, "data", "finetune_dataset_async.jsonl")
    target_dir = os.path.join(llama_factory_dir, "data")
    
    # 确保目标目录存在
    os.makedirs(target_dir, exist_ok=True)
    
    # 复制数据集文件
    import shutil
    shutil.copy(dataset_file, target_dir)
    
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
    dataset_info_path = os.path.join(llama_factory_dir, "data", "dataset_info.json")
    with open(dataset_info_path, "w") as f:
        f.write(dataset_info)

# 启动 WebUI
def start_webui(llama_factory_dir):
    print("启动 LLaMA-Factory WebUI...")
    print("请在浏览器中访问 http://localhost:7860")
    subprocess.run([
        "llamafactory-cli", "webui"
    ], cwd=llama_factory_dir)

if __name__ == "__main__":
    try:
        install_dependencies()
        llama_factory_dir = clone_llama_factory()
        install_llama_factory(llama_factory_dir)
        download_model(llama_factory_dir)
        configure_dataset(llama_factory_dir)
        start_webui(llama_factory_dir)
    except Exception as e:
        print(f"错误: {e}")
        sys.exit(1)
