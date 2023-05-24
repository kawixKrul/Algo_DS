from collections import deque


def bfs(G, s, t):
    """
    O(V+E) - listowa
    O(V^2) - macierzowa
    :param G: graf
    :param s: start
    :param t: koniec
    :return: sciezka w jakiej sa odwiedzane
    """
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

def dfs(G):
    """
    O(V+E) - listowa
    O(V^2) - macierzowa
    :param G: graf
    :return: lista parentow
    """
    def dfs_visit(G, u):
        nonlocal time, visited, parent
        time += 1
        visited[u] = True
        for v in G[u]:
            if not visited[u]:
                parent[v] = u
                dfs_visit(G, v)
        time += 1

    n = len(G)
    parent = [None for _ in range(n)]
    visited = [False for _ in range(n)]
    for v in range(n):
        if not visited[v]:
            dfs_visit(G, v)
    return parent
