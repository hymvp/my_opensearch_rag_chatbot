# models/model_setup.py

from transformers import pipeline
import cohere
import os

def load_model():
    # 获取当前文件所在目录的上一级目录
    base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    model_path = os.path.join(base_path, 'gpt2')

    # 从上一级目录加载文本生成模型
    model = pipeline('text-generation', model=model_path)
    return model
