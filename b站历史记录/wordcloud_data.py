import wordcloud
import jieba
from PIL import Image
f = open('outputs/data.csv', 'r', encoding='utf-8')
lines = f.read()
# s = ''
# for i in lines:
#     s += i
# print(s)
#
# txt=f.read()
# words=jieba.lcut(txt)
# s=' '.join(words)

c = wordcloud.WordCloud(width=1000, font_path="C:\\Windows\\Fonts\\simsun.ttc", height=700)  # 1.配置对象参数
c.generate(lines)  # 2.加载词云文本
c.to_file("outputs/pywordcloud_11.png")  # 3.输出词云文件
