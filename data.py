
if __name__ == '__main__':
    f = open('soc-Epinions1.txt', 'r')
    f.readline()
    f.readline()
    f.readline()
    f.readline()
    edges = [line.strip('\n').split('\t') for line in f]
    f1 = open('data.txt','w')
    for edge in edges:
        f1.write(edge[0]+','+edge[1]+'\n')