from itertools import combinations
import pandas as pd
import numpy as np
import networkx as nx
import networkx.algorithms.community as community
import networkx.algorithms as algo

with open('d:/wrimaga2017-2018.csv','r') as file:
    data = pd.read_csv(file)
    print(data)
    data1 = data.fillna(0)
    train_data = np.array(data1)  # np.ndarray()


    list1 = train_data.tolist()  # 使用list1，list是保留函数
    #print(list1)

    for i in list1:
        for j in i[::-1]:                                #反序遍历不会溢出
            if j == 0:
                i.remove(j)
    #print(list1)

edges = []
for i in list1:
    singleline = combinations(i, 2)
    for j in singleline:
        #a = list(j)                         #使用元祖类型或列表类型都可以作为边加入
        #print(a)
        edges.append(j)

print(edges)

G = nx.Graph()
G.add_edges_from(edges)

print(G.nodes)


