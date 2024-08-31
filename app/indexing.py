# app/indexing.py

from opensearchpy import OpenSearch

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
    client.indices.create(index=index_name, ignore=400)  # 忽略索引已存在的错误

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

    for i, doc in enumerate(documents):
        client.index(index=index_name, id=i, body=doc)

    print("Documents indexed successfully.")
