from math import fabs
from time import time

idx = 0

def PageRank(input_file_name='data.txt',damping_factor=0.85):
    N = 75879
    r = [1. / N for i in range(N)]
    r2 = [1. / N for i in range(N)]
    out_degree = [0 for i in range(N)]
    m = [[] for i in range(N * 2)]
    hash_table = [-1 for i in range(N * 2)]

    eps = 1e-6
    def hash(x):
        global idx
        if hash_table[x] == -1:
            hash_table[x] = idx
            idx += 1
        return hash_table[x]
    def rehash(x):
        for i in range(N):
            if hash(i)==x:
                return i
    data = open(input_file_name)
    for line in data:
        x, y = map(hash, map(int, line.split(',')))
        out_degree[x] += 1
        m[y].append(x)

    t = 0
    begin = time()

    while True:
        for i in range(N):
            r[i] = 0
            for in_id in m[i]:
                r[i] += damping_factor * r2[in_id] / out_degree[in_id]
        der = 1 - sum(r)
        for i in range(N):
            r[i] += der / N

        tag = 0
        for i in range(N):
            if fabs(r[i] - r2[i]) > eps:
                tag = 1
                break
        for i in range(N):
            r2[i] = r[i]
        t += 1
        if tag == 0:
            break

    end = time()
    node_list_in_descending_order = list(range(N))
    r,node_list_in_descending_order=zip(*sorted(zip(r, node_list_in_descending_order), reverse=True))
    node_list_in_descending_order=list(node_list_in_descending_order)
    for i in range(10):
        node_list_in_descending_order[i]=rehash(node_list_in_descending_order[i])
    for i in range(10):
        print('TOP %s\t' %(i+1))
        print(node_list_in_descending_order[i])
        print('Score:')
        print(r[i])
        print('\n')
    print('total iteration is %d' % t)
    print('total time is %f' % (end - begin))
if __name__ == '__main__':
    PageRank()












