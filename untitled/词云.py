import wordcloud
#只留下标题,每个社区里的标题又为一个数组
def titleonly():
    record = []
    for i in community:
        record1 = []
        for j in i:
            sum1 = j.split(" ")
            if len(sum1) > 4:
                record1.append(j)
        record.append(record1)

w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white",max_words=15)
#stopwords = ["IEEEJournals", "Magazine", "Architecture"]
for i in range(0,10):
    str1 = ''.join(record[i])
    #去除停用词
    str2 = str1.replace("IEEE Journals"," ")       #字符串中的替换
    w.generate(str2)
    w.to_file("d:/词云/grwordcloud{}.png".format(i))


#词频统计
import collections
ls = str1.split(" ")
word_counts = collections.Counter(ls)  # 对分词做词频统计
word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
print(word_counts_top10)  # 输出检查