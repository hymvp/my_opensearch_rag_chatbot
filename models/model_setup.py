# models/model_setup.py

from transformers import pipeline

def load_model():
    # 加载文本生成模型
    model = pipeline('text-generation', model='gpt-2')  # 替换为你所需的模型
    return model
