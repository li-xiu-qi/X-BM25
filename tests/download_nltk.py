import nltk

# NLTK 下载选项：用于研究者按需选择数据和模型
# 使用方法：移除所需模块前的 #，运行脚本即可下载对应资源
# 前提：已通过 `pip install nltk` 安装 NLTK 库

# ------------------------------------------------------------------------------
# 综合资源包
# ------------------------------------------------------------------------------
# nltk.download('popular')
#   - 下载 NLTK 的核心资源集合，包括常用预训练模型和小型语料库。
#   - 包含：punkt（分词）、averaged_perceptron_tagger（词性标注）、stopwords（停用词）等。
#   - 大小：约几百 MB
#   - 适用：快速搭建基础自然语言处理流程的研究者。

# nltk.download('all')
#   - 下载 NLTK 的完整资源库，涵盖所有预训练模型、语料库和词典。
#   - 包含：Brown、Treebank、WordNet 等。
#   - 大小：约数 GB
#   - 适用：需要全面数据支持的深入研究，如语义分析、句法解析或大规模语料处理。

# ------------------------------------------------------------------------------
# 独立功能模块
# ------------------------------------------------------------------------------
# nltk.download('punkt')
#   - 下载 Punkt 分词模型，用于词级或句级分割。
#   - 特点：基于无监督学习，支持多语言（以英文为主）。
#   - 适用：文本预处理，如将句子分解为词汇单元或将段落拆分为句子。
#   - 大小：约几十 MB，是大多数后续任务的基础依赖。

# nltk.download('stopwords')
#   - 下载停用词列表，包含多语言（主要为英文）的常见功能词（如 "the"、"and"）。
#   - 适用：文本清洗，移除低信息量词汇以聚焦内容词。
#   - 大小：几 KB
#   - 场景：信息检索或关键词提取。

# nltk.download('averaged_perceptron_tagger')
#   - 下载基于平均感知器的词性标注模型（POS Tagger）。
#   - 功能：为词汇分配语法标签（如 NN 表示名词、VB 表示动词）。
#   - 依赖：punkt 分词结果。
#   - 适用：句法分析或依存解析的前处理。
#   - 大小：约几十 MB。

# nltk.download('wordnet')
#   - 下载 WordNet 词典，一个基于语义关系的词汇数据库。
#   - 功能：提供同义词集（synsets）、上下位关系等。
#   - 大小：约 100 多 MB
#   - 适用：语义分析、词汇扩展或跨语言研究。

# ------------------------------------------------------------------------------
# 语料库资源
# ------------------------------------------------------------------------------
# nltk.download('brown')
#   - 下载 Brown 语料库，一个标注了词性的英文文本集。
#   - 包含：约 100 万词，覆盖新闻、学术、小说等多种体裁。
#   - 适用：词频统计、语言模型训练或文体分析。

# nltk.download('movie_reviews')
#   - 下载电影评论语料库，包含 2000 条带情感标签（正面/负面）的评论。
#   - 适用：情感分析、文本分类或机器学习模型的基准测试。

# nltk.download('treebank')
#   - 下载 Penn Treebank 语料库，包含句法树标注的句子（约 100 万词）。
#   - 适用：句法解析、生成语法研究或依存分析模型的开发与验证。

print("请根据研究需求移除对应模块前的 # 并运行脚本以下载资源。")