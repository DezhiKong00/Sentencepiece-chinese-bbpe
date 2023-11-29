import sentencepiece as spm
spm.SentencePieceTrainer.train(
    input='datasets/train_data.txt',
    model_type="bpe",
    model_prefix='tokenizer',   #输出模型名称前缀。训练完成后将生成 <model_name>.model 和 <model_name>.vocab 文件。
    vocab_size=32000,       #目标词表的大小
    user_defined_symbols=['饕餮', '貔貅'],#可以设置自己特定的token，并且这个token不会被拆成子词
    character_coverage=1,  #覆盖字符的比例
    max_sentencepiece_length=6  #最大的基本单元,也就是在这个单元内的词进行合并
)