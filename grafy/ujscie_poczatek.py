def ujscie(G):
    n = len(G)
    x,y = 0,0
    while x<n and y<n:
        if G[x][y] == 0:
            x += 1
        else:
            y += 1
    for i in range(n):
        if G[y][i] == 1:
            break
        if G[i][y] == 0 and y != i:
            break
    else:
        return y
    return None


def poczatek(G):
    n = len(G)
    time = 0
    visited = [False for _ in range(n)]
    p = [0 for _ in range(n)]

    def dfs(G, s):
        nonlocal time, visited
        visited[s] = True
        time += 1
        for i in G[s]:
            if not visited[G[i]]:
                dfs(G, i)
        time += 1
        p[s] = time

    dfs(G, 0)
    maxi = 0
    for i in range(n):
        if p[i] > p[maxi]:
            maxi = i
    visited = [False for _ in range(n)]
    dfs(G, maxi)
    for el in visited:
        if not el:
            return False
    return True
