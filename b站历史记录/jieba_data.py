# import jieba
#
# f = open('data.csv', 'r', encoding='utf-8')
# lines = f.readlines()
# d = {}
# for l in lines[1:]:
#     s = ''
#     for i in l.split(',')[:-1]:
#         s += i
#     words = jieba.lcut(s)
#     for w in words:
#         if w not in "，。《》？/；’：“‘{}【】=-、 ":
#             d[w] = d.get(w, 0) + 1
# ls = list(d.items())
# ls.sort(key=lambda x: x[1], reverse=True)
# # print(ls)
# for j in range(30):
#     print("{}:{}".format(ls[j][0],ls[j][1]))