from opensearchpy import OpenSearch
from transformers import pipeline
import os
from transformers import AutoModelForCausalLM, AutoTokenizer


# OpenSearch 客户端配置
client = OpenSearch(
    hosts=[{'host': 'localhost', 'port': 9200}],
    http_auth=('username', 'password'),
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

# 获取当前文件所在目录的上一级目录
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base_path, 'gpt2')

# LLM 模型配置，从本地目录加载模型
model_path = './gpt2'

# 从本地路径加载模型和分词器
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)

# 创建文本生成的 pipeline
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)

def search_and_generate(query):
    # 在 OpenSearch 中检索相关文档
    response = client.search(
        index='tech-articles',
        body={
            "query": {
                "match": {
                    "content": query
                }
            }
        }
    )
    
    # 提取搜索结果中的内容
    hits = response['hits']['hits']
    if not hits:
        return "I'm sorry, I couldn't find any information about that."
    
    # 拼接检索到的内容
    context = " ".join(hit["_source"]["content"] for hit in hits)
    
    # 使用 LLM 生成回答
    generated = generator(f"{query} {context}", max_length=100, num_return_sequences=1)
    return generated[0]['generated_text']
