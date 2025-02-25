import jieba


sentence = "@xiaoke，hello！我来自北京清华大学"


# 全模式
seg_list = jieba.cut(sentence, cut_all=True)
print("Full Mode: " + "/ ".join(seg_list))  # 全模式

# 精确模式
seg_list = jieba.cut(sentence, cut_all=False)
print("Default Mode: " + "/ ".join(seg_list))  # 精确模式

