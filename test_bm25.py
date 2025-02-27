from bm25 import load_bm25, create_bm25, bm25_search
import os


# 测试代码
if __name__ == "__main__":
    output_dir = 'test_index_outputs'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # 英文测试
    english_corpus = [
        "this is a sample document about machine learning",
        "machine learning is fascinating and useful",
        "this document discusses deep learning techniques",
        "another sample about artificial intelligence"
    ]
    english_query = "machine learning"
    
    # 创建并保存为 JSON
    bm25_en_json = create_bm25(english_corpus, 'english')
    bm25_en_json.save(os.path.join(output_dir, 'bm25_en.json'))
    
    # 从 JSON 加载并搜索
    loaded_bm25_en_json = load_bm25(os.path.join(output_dir, 'bm25_en.json'), english_corpus)
    print("英文查询（JSON加载）:", english_query)
    results_json = loaded_bm25_en_json.search(english_query, top_k=3)
    for doc_id, score in results_json:
        print(f"文档ID: {doc_id}, 得分: {score:.4f}, 文本: {english_corpus[doc_id]}")
    
    # 创建并保存为 Pickle
    bm25_en_pkl = create_bm25(english_corpus, 'english')
    bm25_en_pkl.save(os.path.join(output_dir, 'bm25_en.pkl'))
    
    # 从 Pickle 加载并搜索
    loaded_bm25_en_pkl = load_bm25(os.path.join(output_dir, 'bm25_en.pkl'), english_corpus)
    print("\n英文查询（Pickle加载）:", english_query)
    results_pkl = loaded_bm25_en_pkl.search(english_query, top_k=3)
    for doc_id, score in results_pkl:
        print(f"文档ID: {doc_id}, 得分: {score:.4f}, 文本: {english_corpus[doc_id]}")
    
    print("\n")

    # 中文测试
    chinese_corpus = [
        "这是一个关于机器学习的样本文档",
        "机器学习既迷人又实用",
        "本文档讨论深度学习技术",
        "另一个关于人工智能的样本"
    ]
    chinese_query = "机器学习"

    # 创建并保存为 JSON
    bm25_cn_json = create_bm25(chinese_corpus, 'chinese')
    bm25_cn_json.save(os.path.join(output_dir, 'bm25_cn.json'))
    
    # 从 JSON 加载并搜索
    loaded_bm25_cn_json = load_bm25(os.path.join(output_dir, 'bm25_cn.json'), chinese_corpus)
    print("中文查询（JSON加载）:", chinese_query)
    results_json = loaded_bm25_cn_json.search(chinese_query, top_k=3)
    for doc_id, score in results_json:
        print(f"文档ID: {doc_id}, 得分: {score:.4f}, 文本: {chinese_corpus[doc_id]}")
    
    # 创建并保存为 Pickle
    bm25_cn_pkl = create_bm25(chinese_corpus, 'chinese')
    bm25_cn_pkl.save(os.path.join(output_dir, 'bm25_cn.pkl'))
    
    # 从 Pickle 加载并搜索
    loaded_bm25_cn_pkl = load_bm25(os.path.join(output_dir, 'bm25_cn.pkl'), chinese_corpus)
    print("\n中文查询（Pickle加载）:", chinese_query)
    results_pkl = loaded_bm25_cn_pkl.search(chinese_query, top_k=3)
    for doc_id, score in results_pkl:
        print(f"文档ID: {doc_id}, 得分: {score:.4f}, 文本: {chinese_corpus[doc_id]}")

    print("\n")

    # 混合语言测试
    mixed_corpus = [
        "this is a sample document about 机器学习",
        "machine learning is fascinating and useful",
        "这是一个关于深度学习的样本文档",
        "another sample about 人工智能"
    ]
    mixed_query = "机器学习"

    # 创建并保存为 JSON
    bm25_mixed_json = create_bm25(mixed_corpus, 'mixed')
    bm25_mixed_json.save(os.path.join(output_dir, 'bm25_mixed.json'))
    
    # 从 JSON 加载并搜索
    loaded_bm25_mixed_json = load_bm25(os.path.join(output_dir, 'bm25_mixed.json'), mixed_corpus)
    print("混合语言查询（JSON加载）:", mixed_query)
    results_json = loaded_bm25_mixed_json.search(mixed_query, top_k=3)
    for doc_id, score in results_json:
        print(f"文档ID: {doc_id}, 得分: {score:.4f}, 文本: {mixed_corpus[doc_id]}")
    
    # 创建并保存为 Pickle
    bm25_mixed_pkl = create_bm25(mixed_corpus, 'mixed')
    bm25_mixed_pkl.save(os.path.join(output_dir, 'bm25_mixed.pkl'))
    
    # 从 Pickle 加载并搜索
    loaded_bm25_mixed_pkl = load_bm25(os.path.join(output_dir, 'bm25_mixed.pkl'), mixed_corpus)
    print("\n混合语言查询（Pickle加载）:", mixed_query)
    results_pkl = loaded_bm25_mixed_pkl.search(mixed_query, top_k=3)
    for doc_id, score in results_pkl:
        print(f"文档ID: {doc_id}, 得分: {score:.4f}, 文本: {mixed_corpus[doc_id]}")


    # 测试bm25_search
    print("\n")
    print("测试bm25_search")
    results = bm25_search(corpus=english_corpus,query="machine learning")
    print("英文查询:", "machine learning")
    for doc_id, score,doc in results:
        print(f"文档ID: {doc_id}, 得分: {score:.4f}, 文本: {doc}")