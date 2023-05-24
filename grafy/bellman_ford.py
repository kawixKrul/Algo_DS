from math import inf


def bellman_ford(graph, start):
    V = len(graph)
    dist = [inf] * V
    dist[start] = 0

    for _ in range(V - 1):
        for u in range(V):
            for v, weight in graph[u]:
                if dist[u] != inf and dist[u] + weight < dist[v]:
                    dist[v] = dist[u] + weight

    for u in range(V):
        for v, weight in graph[u]:
            if dist[u] != inf and dist[u] + weight < dist[v]:
                return None

    return dist


graph = [
    [(1, 3), (2, 6)],
    [(2, 2), (3, 1)],
    [(3, 1)],
    [(0, 4), (1, 2)],
]


distances = bellman_ford(graph, 0)
print(distances)