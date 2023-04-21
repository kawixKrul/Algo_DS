from zad4testy import runtests
from collections import deque

""" 
algorytm szuka najkrotszej sciezki pomiedzy zadanymi wierzcholkami uzywajac algorytmu BFS
, potem na jej podstawie tworzy nowy graf z usunieta krawedzia i szuka najkrotszej sciezki dla niego. 
 Zeby sprawdzic czy krawedz spelnia warunki zadania nastepuje porownanie dlugosci 2 sciezek
 zlozonosc: O(n*(V+E)) gdzie n to dlgosc najkrotszej sciezki
"""


def longer( G, s, t ):
    def bfs(G, s, t):
        n = len(G)
        visited = [False for _ in range(n)]
        queue = deque([(s, [s])])
        while queue:
            (v, path) = queue.popleft()
            if v == t:
                return path
            if not visited[v]:
                visited[v] = True
                for neighbor in G[v]:
                    if not visited[neighbor]:
                        queue.append((neighbor, path + [neighbor]))
        return None

    def remove_E(G, E):
        G[E[0]].remove(E[1])
        G[E[1]].remove(E[0])
        return G

    removed = []
    path = bfs(G,s,t)
    p_len = len(path)
    if path is None:
        return None
    for i in range(1, p_len):
        edge = (path[i-1], path[i])
        new = remove_E(G,edge)
        p_new = bfs(new, s, t)
        if p_new is None or len(p_new) > p_len:
            removed.append(edge)
    if removed:
        return removed[0]
    else:
        return None

# zmien all_tests na True zeby uruchomic wszystkie testy
runtests( longer, all_tests = True )