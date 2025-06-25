def bfs(start_node, graph):
    visited = set()
    queue = [start_node]
    visited.add(start_node)

    while queue:
        node = queue.pop(0)
        print("Visiting:", node)

        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Driver Code
graph = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

start_node = 0
bfs(start_node, graph)
