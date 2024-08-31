# models/model_setup.py

from transformers import pipeline
import cohere
import os

def load_model():
    # 获取当前文件所在目录的上一级目录
    model = pipeline('text-generation', model='./gpt2')
    return model
