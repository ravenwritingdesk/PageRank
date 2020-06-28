#2018202114-PageRank.py
#Copyright © 2020 - by Wangchuwen，RUC.All rights reserved。


import numpy as np
#import time

def PageRank(input_file_name='data.txt',damping_factor=0.85):

    # 读入有向图，存储边
    f = open(input_file_name, 'r')
    edges = [line.strip('\n').split(',') for line in f]
    #print(edges)
    # 根据边获取节点的集合
    nodes = []
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])
    #print(nodes)

    #获取节点个数，并将节点按名称排好
    N = len(nodes)
    nodes.sort()

    # 将节点符号（字母），映射成阿拉伯数字，便于后面生成A矩阵/S矩阵，
    # 如果原来节点符号就是数字，可以将这一部分注释掉
    i = 0
    node_to_num = {}
    for node in nodes:
        node_to_num[node] = i
        i += 1
    for edge in edges:
        edge[0] = node_to_num[edge[0]]
        edge[1] = node_to_num[edge[1]]
    #print(edges)


    # 生成初步的S矩阵,（邻接矩阵转置）
    S = np.zeros([N, N])
    for edge in edges:
        S[edge[1], edge[0]] = 1#remark：这里的S是邻接矩阵的转置
    #print(S)

    # 计算比例：即一个网页对其他网页的PageRank值的贡献，即进行列的归一化处理
    for j in range(N):
        sum_of_col = sum(S[:, j])
        for i in range(N):
            if sum_of_col!=0:
                S[i, j] /= sum_of_col#remark：这里的S相当于L=M^（-1）*A
            else:
                 S[i,j] = 1/N#如果有出度为0的点，则加边
    #print(S)


    # 计算矩阵A
    A = damping_factor * S + (1 - damping_factor) / N * np.ones([N, N])
    #print(A)

    # 生成初始的PageRank值，记录在P_n中，P_n和P_n1均用于迭代
    P_n = np.ones(N) / N
    P_n1 = np.zeros(N)

    e = 100000  # 误差初始化
    #k = 0  # 记录迭代次数

    while e > 0.000001:  # 开始迭代
        P_n1 = np.dot(A, P_n)  # 迭代公式
        e = P_n1 - P_n
        e = max(map(abs, e))  # 计算误差
        P_n = P_n1
        #k += 1
        #print('iteration %s:' % str(k), P_n1)

    #按照各节点的分数给节点列表排序
    P_n,node_list_in_descending_order=zip(*sorted(zip(P_n,nodes),reverse=True))
    #化为list
    node_list_in_descending_order=list(node_list_in_descending_order)
    return node_list_in_descending_order







def PPR(input_Graph='data.txt' , input_Seed='seeds.txt' , damping_factor=0.85 ) :
    # 读入有向图，存储边
    f = open(input_Graph, 'r')
    edges = [line.strip('\n').split(',') for line in f]
    #print(edges)

    # 根据边获取节点的集合
    nodes = []
    for edge in edges:
        if edge[0] not in nodes:
            nodes.append(edge[0])
        if edge[1] not in nodes:
            nodes.append(edge[1])
    #print(nodes)

    # 获取节点个数，并将节点按名称排好
    N = len(nodes)
    nodes.sort()

    # 将节点符号（字母），映射成阿拉伯数字，便于后面生成A矩阵/S矩阵
    i = 0
    node_to_num = {}
    for node in nodes:
        node_to_num[node] = i
        i += 1
    for edge in edges:
        edge[0] = node_to_num[edge[0]]
        edge[1] = node_to_num[edge[1]]
    #print(edges)



    # 生成初步的S矩阵
    S = np.zeros([N, N])
    for edge in edges:
        S[edge[1], edge[0]] = 1
    #print(S)

    # 计算比例：即一个网页对其他网页的PageRank值的贡献，即进行列的归一化处理
    for j in range(N):
        sum_of_col = sum(S[:, j])
        for i in range(N):
            if sum_of_col != 0:
                S[i, j] /= sum_of_col  # remark：这里的S相当于L=M^（-1）*A
            else:
                S[i, j] = 1 / N  # 如果有出度为0的点，则加边
    #print(S)

    #载入种子文件
    f2 = open(input_Seed, 'r')
    seeds = [line.strip('\n').split(',') for line in f2]
    p_init=[0]*N
    for seed in seeds:
        p_init[node_to_num[seed[0]]]=seed[1]#初始化
    #print(p_init)
    p_init=np.array(p_init,'float64')#list类型变为float，便于计算

    # 计算矩阵A
    A = damping_factor * S
    #print(A)

    # 生成初始的PageRank值，记录在P_n中，P_n和P_n1均用于迭代
    P_n = p_init
    P_n1 = np.zeros(N)

    e = 100000  # 误差初始化
    #k = 0  # 记录迭代次数


    while e > 0.000001:  # 开始迭代
        P_n1 = np.dot(A, P_n)+(1-damping_factor)*p_init # 迭代公式
        e = P_n1 - P_n
        e = max(map(abs, e))  # 计算误差
        P_n = P_n1
        #k += 1
        #print('iteration %s:' % str(k), P_n1)

    # 按照各节点的分数给节点列表排序
    P_n, node_list_in_descending_order = zip(*sorted(zip(P_n, nodes), reverse=True))
    # 化为list
    node_list_in_descending_order = list(node_list_in_descending_order)
    return node_list_in_descending_order

