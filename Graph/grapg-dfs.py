def dfs(node, graph, visited):
    print("Visiting:", node)
    visited.add(node)

    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, graph, visited)

# Driver Code
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

visited = set()
start_node = 0
dfs(start_node, graph, visited)
