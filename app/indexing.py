# app/indexing.py

from opensearchpy import OpenSearch
from opensearchpy.exceptions import OpenSearchException

# OpenSearch 客户端配置
client = OpenSearch(
    hosts=[{'host': 'amaaaaaaak7gbrianb7fygags7cumwx6qfkd5z6ljuftaghnw3ee6ievxtuq.opensearch.us-ashburn-1.oci.oraclecloud.com', 'port': 9200}],
    http_auth=('hanyong', 'Hanyong0618@'),
    use_ssl=True,
    verify_certs=False,
    ssl_assert_hostname=False,
    ssl_show_warn=False,
)

# 创建索引并添加文档
def index_documents():
    index_name = 'tech-articles'
    
    try:
        # 创建索引
        response = client.indices.create(index=index_name, ignore=400)  # 忽略索引已存在的错误
        if 'acknowledged' in response:
            print(f"Index '{index_name}' created successfully.")
        else:
            print(f"Index '{index_name}' already exists or creation failed.")
        
        documents = [
            {
                "title": "What is Python?",
                "content": "Python is a popular programming language known for its simplicity and versatility."
            },
            {
                "title": "Getting started with Flask",
                "content": "Flask is a lightweight WSGI web application framework in Python."
            }
        ]

        # 索引文档
        for i, doc in enumerate(documents):
            response = client.index(index=index_name, id=i, body=doc)
            if 'result' in response:
                print(f"Document ID {i} indexed successfully with result: {response['result']}.")
            else:
                print(f"Failed to index document ID {i}.")
    
    except OpenSearchException as e:
        print(f"An error occurred while indexing documents: {e}")

# 调用索引函数
if __name__ == "__main__":
    print("Starting the indexing process...")
    index_documents()
    print("Indexing process completed.")
