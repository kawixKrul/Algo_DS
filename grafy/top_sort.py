def topological_sort(graph):
    visited = [False] * len(graph)
    stack = []

    def dfs(vertex):
        visited[vertex] = True

        for neighbor in graph[vertex]:
            if not visited[neighbor]:
                dfs(neighbor)

        stack.append(vertex)

    for vertex in range(len(graph)):
        if not visited[vertex]:
            dfs(vertex)

    stack.reverse()
    return stack


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E', 'F']
    graph = [
        [],  # Vertex 0: A (no dependencies)
        [],  # Vertex 1: B (no dependencies)
        [],  # Vertex 2: C (no dependencies)
        [1, 2],  # Vertex 3: D (depends on B and C)
        [3, 4],  # Vertex 4: E (depends on D and E)
        [5],  # Vertex 5: F (depends on E)
    ]

    # Perform topological sort
    result = topological_sort(graph)

    # Print the sorted order
    sorted_order = [vertices[vertex] for vertex in result]
    print("Topological Sort:", sorted_order)