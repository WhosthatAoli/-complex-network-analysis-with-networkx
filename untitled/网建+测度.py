from itertools import combinations
import pandas as pd
import numpy as np
import networkx as nx
import networkx.algorithms.community as community
import networkx.algorithms as algo

def GraphBuild():
    with open('d:/wrimaga2017-2018.csv', 'r') as file:
        data = pd.read_csv(file)
        print(data)
        data1 = data.fillna(0)
        train_data = np.array(data1)  # np.ndarray()

        list1 = train_data.tolist()  # 使用list1，list是保留函数
        # print(list1)

        for i in list1:
            for j in i[::-1]:  # 反序遍历不会溢出
                if j == 0:
                    i.remove(j)
        # print(list1)

    edges = []
    for i in list1:
        singleline = combinations(i, 2)
        for j in singleline:
            # a = list(j)                         #使用元祖类型或列表类型都可以作为边加入
            # print(a)
            edges.append(j)

    #print(edges)

    G = nx.Graph()
    G.add_edges_from(edges)
    return G

def degreelist():
    degree = G.degree
    import csv
    with open('d:/degree.csv', 'w', encoding='gb18030') as f:
        f = csv.writer(f)
        f.writerows(degree)

def computeCentrality():
    central = algo.degree_centrality(G)                                       #度中心性 central为字典，使用.item变成可sorted的
    centralRank=sorted(central.items(),key=lambda x:x[1],reverse=True)            #字典排序 False从小到大 Ture从大到小
    harmonic = nx.algorithms.centrality.harmonic_centrality(G)
    harmonicRank = sorted(harmonic.items(), key=lambda x: x[1], reverse=True)
    closeness = nx.closeness_centrality(G)
    closenessRank = sorted(closeness.items(), key=lambda x: x[1], reverse=True)
    betweenness = nx.betweenness_centrality(G)
    betweennessRank = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)
    return harmonicRank, closenessRank, betweennessRank


def computeCommunity():
    import wordcloud
    community = nx.algorithms.community.greedy_modularity_communities(G)
    return community
    #只留下标题,每个社区里的标题又为一个数组
    record = []
    for i in community:
        record1 = []
        for j in i:
            sum1 = j.split(" ")
            if len(sum1) > 4:
                record1.append(j)
        record.append(record1)

    w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700, background_color="white", max_words=15)
    # stopwords = ["IEEEJournals", "Magazine", "Architecture"]
    for i in range(0, 10):
        str1 = ''.join(record[i])
        # 去除停用词
        str2 = str1.replace("IEEE Journals", " ")  # 字符串中的替换
        w.generate(str2)
        w.to_file("d:/词云2017/grwordcloud{}.png".format(i))

    # 词频统计
    import collections
    ls = str1.split(" ")
    word_counts = collections.Counter(ls)  # 对分词做词频统计
    word_counts_top10 = word_counts.most_common(10)  # 获取前10最高频的词
    print(word_counts_top10)  # 输出检查

def cluster():
    cluster = nx.clustering(G, nodes=None, weight=None)
    clusteringIndex = nx.average_clustering(G, nodes=None, weight=None, count_zeros=True)
    return clusteringIndex

def pagerank():
    importantnode = nx.pagerank(G)                                               #pagerank算法查找网络中的重要节点
    pagerank =sorted(importantnode.items(),key=lambda x:x[1],reverse=True)       #字典排序 False从小到大 Ture从大到小
    return  pagerank

if __name__ == '__main__':
    G = GraphBuild()
    #degreelist()
    print(G.number_of_nodes())                                                         #点的个数
    density = nx.density(G)
    #nx.average_shortest_path_length(G, weight=None, method=None)                #平均路径长度,，必须要在网络全部连通的情况下使用
    harmonicRank, closenessRank, betweennessRank = computeCentrality()[0], computeCentrality()[1], computeCentrality()[2]
    community = computeCommunity()
    pagerank = pagerank()
    averageCluster = cluster()