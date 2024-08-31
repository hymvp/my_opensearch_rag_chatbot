import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

from opensearchpy import OpenSearch
from transformers import pipeline
import os
from transformers import AutoModelForCausalLM, AutoTokenizer


# OpenSearch 客户端配置
logger.info("Initializing OpenSearch client...")
client = OpenSearch(
    hosts=[{'host': 'amaaaaaaak7gbrianb7fygags7cumwx6qfkd5z6ljuftaghnw3ee6ievxtuq.opensearch.us-ashburn-1.oci.oraclecloud.com', 'port': 9200}],
    http_auth=('hanyong', 'Hanyong0618@'),
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)
logger.info("OpenSearch client initialized successfully.")


# 获取当前文件所在目录的上一级目录
logger.info("Getting base path...")
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(base_path, 'gpt2')
logger.info(f"Base path: {base_path}, Model path: {model_path}")


# LLM 模型配置，从本地目录加载模型
logger.info("Loading LLM model from local directory...")
model_path = './gpt2'
logger.info(f"Model path: {model_path}")

# 从本地路径加载模型和分词器
logger.info("Loading model and tokenizer from local path...")
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(model_path)
logger.info("Model and tokenizer loaded successfully.")


# 创建文本生成的 pipeline
logger.info("Creating text generation pipeline...")
generator = pipeline('text-generation', model=model, tokenizer=tokenizer)
logger.info("Text generation pipeline created successfully.")


def search_and_generate(query):
    logger.info(f"Searching for query: {query}...")
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
    logger.info("Search completed.")
    
    # 提取搜索结果中的内容
    hits = response['hits']['hits']
    if not hits:
        logger.info("No hits found.")
        return "I'm sorry, I couldn't find any information about that."
    
    # 拼接检索到的内容
    context = " ".join(hit["_source"]["content"] for hit in hits)
    logger.info("Context generated.")
    
    # 使用 LLM 生成回答
    logger.info("Generating answer using LLM...")
    generated = generator(f"{query} {context}", max_length=100, num_return_sequences=1)
    return generated[0]['generated_text']
										 
