from zad5testy import runtests
from queue import PriorityQueue
from math import inf

'''
algorytm przeksztalca liste z krawedziami E i osobliwosciami S w graf G, gdzie osobliwosci sa poloczone miedzy
soba krawedziami o wadze 0 i do unormowane sa poloczenia z wierzcholkami wspolnymi do najnizszej wagi sposrod 
odpowiednich par wierzcholkow. Nastepnie na takim grafie dziala algorytm Dijkstry ktory znajduje najkrotsza 
sciezke z a do b
zlozonosc O(E+ ElogV)
'''


def spacetravel( n, E, S, a, b ):

    def relax(u,v,l,d,queue):
        if d[v] > d[u] + l:
            d[v] = d[u] + l
            queue.put((d[v],v))

    def dijkstra(G):
        nonlocal n,a
        d = [inf for _ in range(n)]
        d[a] = 0
        queue = PriorityQueue()
        queue.put((d[a],a))
        while not queue.empty():
            du, u = queue.get()
            if d[u] == du:
                for v, l in G[u]:
                    relax(u,v,l,d,queue)
        return d

    def graf():
        nonlocal n, E,S
        G = [[] for _ in range(n)]
        for s, t, w in E:
            G[s].append([t,w])
            G[t].append([s,w])
        distinct = [[] for _ in range(n)]
        for v in S:
            for x in G[v]:
                distinct[x[0]].append(x)
        for d in distinct:
            d.sort(key=lambda z: z[1])
        for v in S:
            for i in range(len(G[v])):
                G[v][i][1] = distinct[G[v][i][0]][0][1]
        for v in S:
            for u in S:
                if v != u:
                    G[v].append([u,0])
        return G

    g = graf()
    dist = dijkstra(g)

    return dist[b] if dist[b] != inf else None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( spacetravel, all_tests = True )
