#部分数据集空格较多，大多数为无用字符，需要移除。
sentences = []
with open("datasets/明朝那些事儿.txt",encoding="ansi") as file:   #加载文档
    data = file.read().split("\n")
for row in data:        #删除无用字符
    row = row.strip()
    sentences.append(row)
# print(sentence)
with open("datasets/train_data.txt", "w", encoding="utf-8") as file:
    file.write("\n".join(sentences))
