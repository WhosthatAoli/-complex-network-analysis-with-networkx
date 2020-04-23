import networkx as nx
import networkx.algorithms.community as community
import networkx.algorithms as algo

G.number_of_nodes()                                                         #点的个数
nx.average_shortest_path_length(G, weight=None, method=None)                #平均路径长度


#计算所有节点的度，并保存在csv文件中
def degreelist():
    degree = G.degree
    import csv
    with open('d:/degree.csv', 'w', encoding='gb18030') as f:
        f = csv.writer(f)
        f.writerows(degree)

#Geiph出图
def Geiphgraph():
    nx.write_gexf(G,'your_file_name.gexf')

#中心性计算
def computeCentrality():
    central = algo.degree_centrality(G)                                       #度中心性 central为字典，使用.item变成可sorted的
    centralRank=sorted(central.items(),key=lambda x:x[1],reverse=True)            #字典排序 False从小到大 Ture从大到小
    harmonic = nx.algorithms.centrality.harmonic_centrality(G)
    harmonicRank = sorted(harmonic.items(), key=lambda x: x[1], reverse=True)
    closeness = nx.closeness_centrality(G)
    closenessRank = sorted(closeness.items(), key=lambda x: x[1], reverse=True)
    betweenness = nx.betweenness_centrality(G)
    betweennessRank = sorted(betweenness.items(), key=lambda x: x[1], reverse=True)


#社区发现与关键词
def computerCommunity():
    community = community.greedy_modularity_communities(G)
    #只留下标题,每个社区里的标题又为一个数组
    record = []
    for i in community:
        record1 = []
        for j in i:
            sum1 = j.split(" ")
            if len(sum1) > 4:
                record1.append(j)
        record.append(record1)

def pagerank():
    importantnode = nx.pagerank(G)                                               #pagerank算法查找网络中的重要节点
    pagerank =sorted(importantnode.items(),key=lambda x:x[1],reverse=True)            #字典排序 False从小到大 Ture从大到小

#小世界
def littleWorld():
    nx.random_reference(G[, niter, connectivity, seed])
    #Compute a random graph by swapping edges of a given graph.
    nx.lattice_reference(G[, niter, D, …])
    #Latticize the given graph by swapping edges.
    nx.sigma(G[, niter, nrand, seed])                            #A graph is commonly classified as small-world if sigma>1.
    #Returns the small-world coefficient (sigma) of the given graph.
    nx.omega(G[, niter, nrand, seed])             #The small-world coefficient (omega) ranges between -1 and 1. Values close to 0 means the G features small-world characteristics. Values close to -1 means G has a lattice shape whereas values close to 1 means G is a random graph.
    #Returns the small-world coefficient (omega) of a graph

def cluster():
    nx.clustering(G, nodes=None, weight=None)
    nx.average_clustering(G, nodes=None, weight=None, count_zeros=True)


