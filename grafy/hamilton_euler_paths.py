from top_sort import topological_sort


def hamiltonian_path(graph):
    topological_order = topological_sort(graph)

    for i in range(len(topological_order) - 1):
        current_vertex = topological_order[i]
        next_vertex = topological_order[i + 1]

        if next_vertex not in graph[current_vertex]:
            return False

    return True


def euler_path(G):
    n = len(G)
    visited = [False for _ in range(n)]
    result = []

    def dfs(G, s):
        nonlocal visited, result
        for i in range(n):
            if G[s][i] == 1:
                G[s][i], G[i][s] = 0,0
                dfs(G, i)
        result.append(s)


if __name__ == "__main__":
    graph = [
        [1, 2],  # Vertex 0: A (depends on B and C)
        [3],     # Vertex 1: B (depends on D)
        [3, 4],  # Vertex 2: C (depends on D and E)
        [4],     # Vertex 3: D (depends on E)
        []       # Vertex 4: E (no dependencies)
    ]

    graph2 = [
        [1, 2],  # Vertex 0: A (depends on B and C)
        [3],     # Vertex 1: B (depends on D)
        [3, 4],  # Vertex 2: C (depends on D and E)
        [4],     # Vertex 3: D (depends on E)
        [5],     # Vertex 4: E (depends on F)
        [1,2,3,4]       # Vertex 5:
    ]

    if hamiltonian_path(graph):
        print("The graph contains a Hamiltonian path")
    else:
        print("The graph does not contain a Hamiltonian path")

    if hamiltonian_path(graph2):
        print("The graph contains a Hamiltonian path")
    else:
        print("The graph does not contain a Hamiltonian path")