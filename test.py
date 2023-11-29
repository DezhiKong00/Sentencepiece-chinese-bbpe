import sentencepiece as spm

# 加载训练好的模型
model_path = "tokenizer.model"
tokenizer = spm.SentencePieceProcessor()
tokenizer.load(model_path)

# 测试分词器
text = "饕餮和貔貅是中国传统文化中的神兽。"
tokens = tokenizer.encode_as_pieces(text)

print("分词结果:", tokens)