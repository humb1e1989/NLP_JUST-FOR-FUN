import nltk
from nltk.tokenize import wordpunct_tokenize as wd
import re
# 还有少量的非文本内容的可以直接用Python 的正则表达式(re)删除
# 另外还有一些特殊的非英文字符和标点符号,也可以用Python的正则表达式(re)删除。
import matplotlib.pyplot as plt
from collections import Counter
# 读取文件
txt = open("mobydick.txt", "r", encoding="gb18030").read()
# 转统一大小写
txt = txt.lower()
# 数据清理， 将除了a-z A-Z 0-9 之外的符号全部都换成空格
txt = re.sub(r'[^a-zA-Z0-9]', " ", txt)
# 除去html标签
# cleanr = re.compile('<.*?>')
# txt = re.sub(cleanr, ' ', txt)
# 分词
words = wd(txt)
# 遍历计数
counts = {} # {"word":2}
# counts是字典， word 是key words 也是字典（前面是value 后面是key，key在这个里面就是）
# 将数据导入到字典counts中
for word in words:
    # dict[key] -> value // dict[key]/dict.get(key, def)
    counts[word] = counts.get(word, 0) + 1
#     get word 是值（分词出来的词），0是def的值 + 1 完全是为了计数）
# 返回遍历得到的键与值并排序
# item这里是元组 就是把value和key绑在一起了 需要转化成list
items = list(counts.items())
# 排序 讲item排序 逆序 用了lambda函数，从x参数的第一个开始排
items.sort(key=lambda x: x[1], reverse=True)
# 重新按照reverse的顺序 排count的value 也就是出现的频次
sort_list = sorted(counts.values(), reverse=True)
# 计数 遍历item list
counter = 0
for item in items:
    counter = counter + 1
for i in range(counter):
    word, count = items[i]
    print("{0:<10}{1:>5}".format(word, count))

# 用matplotlib验证Zipf-Law并出图
# Zipf 第一定律——二八原则。在自然语言文本（集）中，按着词的出现频率（f）降序排序，那么频率和序（r）之间有近似幂律关系。
plt.title('Zipf‘s Law',fontsize=18)  #标题
plt.xlabel('Ranking',fontsize=18)     #排名
plt.ylabel('Frequency',fontsize=18)     #频度
plt.yticks([pow(10,i) for i in range(0,)])  # 设置y刻度
plt.xticks([pow(10,i) for i in range(0,)])  # 设置x刻度
x = [i for i in range(len(sort_list))]
# 对数坐标：对变元取对数，“压缩”了变化范围。将一个数量级压缩在一个单位之内。因此，数量越大，压缩得越严重
plt.yscale('log')                  #设置纵坐标的缩放
plt.xscale('log')                  #设置横坐标的缩放
plt.plot(x,sort_list , 'pink')       #绘图
plt.savefig('./Zipf‘s Law.jpg')      #保存图片
plt.show()
# 统计前20个
wordcount = 20
plt.figure()
# 计数 计算总词数
counterall = 0
for word in words:
    counterall= counterall + 1
# word1, count1 = items[0]
# 考虑到最多的词在一个大型词料库中 最多的词占据7%-10% 所以设置横坐标为要展示的词的个数 纵坐标为总词数的10%
plt.axis([0,wordcount,0,counterall * 0.1])
# 避免x轴的label重合， 选择合适的字体大小和旋转角度展示
plt.xticks(rotation=-15)
plt.tick_params(axis='x', labelsize=9)
plt.title('Bar result of Zipf‘s Law')
for i in range(wordcount):
    word, count = items[i]
    # 横坐标为word 就是分词出来的单词，纵坐标为count，为对应单词的出现频次（已经sort过了 所以是一一对应的）
    plt.bar(word, count)
    plt.savefig('.Bar result of Zipf‘s Law.jpg')  # 保存图片
plt.show()
