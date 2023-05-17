from collections import deque


def bfs(G):
    n = len(G)
    visited = [False for _ in range(n)]
    queue = deque()
    
