import heapq
from kruskal import graph

def prim(G):
    n = len(G)
    visited = [False for _ in range(n)]
    min_heap = []
    mst = []
    visited[0] = True

    for edge in graph[0]:
        heapq.heappush(min_heap, (*edge, 0))

    while min_heap:
        weight, v, u = heapq.heappop(min_heap)
        if visited[v]:
            continue

        visited[v] = True
        mst.append((weight, u, v))

        for edge in graph[v]:
            if not visited[edge[1]]:
                heapq.heappush(min_heap, (*edge, v))

    return mst


min_spanning_tree = prim(graph)
print(min_spanning_tree)
