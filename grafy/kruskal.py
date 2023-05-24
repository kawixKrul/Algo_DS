class FindUnion:
    def __init__(self, n):
        self.parent = [x for x in range(n)]
        self.rank = [0 for _ in range(n)]

    def find_root(self, v):
        if self.parent[v] != v:
            self.parent[v] = self.find_root(self.parent[v])
        return self.parent[v]

    def union(self, x, y):
        x_root = self.find_root(x)
        y_root = self.find_root(y)

        if x_root == y_root:
            return False

        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] += 1

        return True


def kruskal(graph):
    V = len(graph)
    edges = []
    mst = []
    for u in range(V):
        for weight, v in graph[u]:
            edges.append((weight, u, v))
    edges.sort()  # Sortowanie krawędzi rosnąco względem wag

    union_find = FindUnion(V)

    for edge in edges:
        weight, u, v = edge
        if union_find.union(u, v):
            mst.append(edge)

    return mst


graph = [
    [(4, 1), (1, 3)],           # Vertex 0
    [(4, 0), (2, 3), (3, 2)],   # Vertex 1
    [(5, 2), (1, 0), (3, 1)],   # Vertex 2
    [(2, 1), (1, 2)]            # Vertex 3
]

min_spanning_tree = kruskal(graph)
print(min_spanning_tree)