from bm25 import bm25_search


if __name__ == "__main__":
    # 英文测试
    english_corpus = [
        "this is a sample document about machine learning",
        "machine learning is fascinating and useful",
        "this document discusses deep learning techniques",
        "another sample about artificial intelligence"
    ]
    english_query = "machine learning"
    english_results = bm25_search(english_corpus, english_query, 'english', top_k=3)
    print("英文查询:", english_query)
    for doc_id, score, text in english_results:
        print(f"文档ID: {doc_id}, 得分: {score:.4f}, 文本: {text}")

    print("\n")

    # 中文测试
    chinese_corpus = [
        "这是一个关于机器学习的样本文档",
        "机器学习既迷人又实用",
        "本文档讨论深度学习技术",
        "另一个关于人工智能的样本"
    ]
    chinese_query = "机器学习"
    chinese_results = bm25_search(chinese_corpus, chinese_query, 'chinese', top_k=3)
    print("中文查询:", chinese_query)
    for doc_id, score, text in chinese_results:
        print(f"文档ID: {doc_id}, 得分: {score:.4f}, 文本: {text}")