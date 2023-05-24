from math import inf


def floyd_warshall(graph):
    V = len(graph)
    dist = [[0 if i == j else inf for j in range(V)] for i in range(V)]

    # Inicjalizacja macierzy odległości na podstawie grafu
    for u in range(V):
        for v, weight in graph[u]:
            dist[u][v] = weight

    # Wykonanie relaksacji dla wszystkich par wierzchołków
    for k in range(V):
        for u in range(V):
            for v in range(V):
                dist[u][v] = min(dist[u][v], dist[u][k] + dist[k][v])

    return dist


# Graf ważony skierowany
graph = [
    [(1, 3), (2, 6)],
    [(2, 2), (3, 1)],
    [(3, 1)],
    [(0, 4), (1, 2)],
]

distances = floyd_warshall(graph)
print(distances)