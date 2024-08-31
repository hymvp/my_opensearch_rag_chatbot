# models/model_setup.py

from transformers import pipeline
import cohere

def setup_model():
    # 初始化 Cohere 客户端
    model = pipeline('text-generation', model='./gpt2')
    return model
