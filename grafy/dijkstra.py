from math import inf
from queue import PriorityQueue
from top_sort import topological_sort


def relax(u, v, l, d, parent, queue):
    if d[v] > d[u] + l:
        d[v] = d[u] + l
        parent[v] = u
        queue.put((d[v], v))


def dijkstra(G,s):
    n = len(G)
    parent = [None for _ in range(n)]
    d = [inf for _ in range(n)]
    d[s] = 0
    queue = PriorityQueue()
    queue.put((d[s], s))
    while not queue.empty():
        du, u = queue.get()
        if d[u] == du:
            for v, l in G[u]:
                relax(u, v, l, d, parent, queue)
    return d, parent


# shortest path in DAG
def dag_shortest(G, s, t):
    n = len(G)
    sorted_g = topological_sort(G)
    d = [inf for _ in range(n)]
    parent = [None for _ in range(n)]
    for id in range(sorted_g.index(s)+1, n):
        for p, l in G[id]:
            if d[p] == d[id] + l:
                parent[p] = id
    return d, parent


# print paths
def print_path_rec(start, u, parent):
    if start == u:
        print(u)
    else:
        print_path_rec(start, parent[u], parent)
    print(u)


def print_path(start, u, parent):
    path = [u]
    while u != start:
        u = parent[u]
        path.append(u)
    print(path[::-1])
