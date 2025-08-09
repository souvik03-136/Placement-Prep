# Problem Statement
# You are given an undirected graph with n nodes (numbered 0 to n-1) and a list of edges.
#
# Your task is:
#
# Check if there exists any single edge whose removal will make at least one node unreachable from some other node in the graph (i.e., the graph becomes disconnected).
#
# If there are multiple such edges, return any one of them (in the form [u, v] where u < v).
#
# If removing any single edge still keeps the graph fully connected (all nodes reachable from each other), return -1.
#
# Example 1
#
# lua
# Copy
# Edit
# Input:
# n = 4
# edges = [[0,1], [0,2], [0,3], [2,3]]
#
# Output:
# [0,1]
# Explanation: Removing edge 0-1 will make node 1 isolated and unreachable from other nodes.
#


def find_bridge(n, edges):
    from collections import defaultdict, deque

    # Function to check connectivity
    def is_connected(n, adj):
        visited = set()
        q = deque([0])
        visited.add(0)

        while q:
            node = q.popleft()
            for nei in adj[node]:
                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return len(visited) == n

    # Try removing each edge one by one
    for u, v in edges:
        # Build adjacency list without this edge
        adj = defaultdict(list)
        for x, y in edges:
            if (x, y) == (u, v) or (x, y) == (v, u):
                continue
            adj[x].append(y)
            adj[y].append(x)

        # Check if graph is connected
        if not is_connected(n, adj):
            return [u, v] if u < v else [v, u]

    return -1

n = 4
edges = [[0,1],[0,2],[0,3],[2,3]]
print(find_bridge(n, edges))  # Output: [0,1]

n = 4
edges = [[0,1],[1,2],[2,3],[3,0]]
print(find_bridge(n, edges))  # Output: -1


#
# see exactly what’s happening.
#
# Example Graph
# ini
# Copy
# Edit
# n = 4
# edges = [
#     [0, 1],
#     [1, 2],
#     [2, 3]
# ]
# This is just a straight line:
#
# lua
# Copy
# Edit
# 0 -- 1 -- 2 -- 3
# Step-by-Step Process
# Step 1 — Try removing each edge one by one
# We’ll loop through all edges and check connectivity.
#
# Case 1: Remove edge [0, 1]
# Remaining edges:
#
# csharp
# Copy
# Edit
# [1, 2]
# [2, 3]
# Adjacency list now:
#
# makefile
# Copy
# Edit
# 0: []
# 1: [2]
# 2: [1, 3]
# 3: [2]
# BFS starting from 0:
#
# Start at 0 → visited = {0}
#
# No neighbors → BFS stops
#
# Visited nodes = {0}, but we need all {0,1,2,3} → Graph is disconnected ✅
#
# Conclusion: [0, 1] is a bridge → return it.
#
# We don’t even need to check the other edges because we already found one bridge.
#
# If we continued anyway:
# Case 2: Remove edge [1, 2]
# Remaining edges:
#
# csharp
# Copy
# Edit
# [0, 1]
# [2, 3]
# BFS from 0:
#
# Visit 0 → {0}
#
# Go to 1 → {0, 1}
#
# No connection to 2 → stops early
#
# Disconnected again ✅
#
# Case 3: Remove edge [2, 3]
# Remaining edges:
#
# csharp
# Copy
# Edit
# [0, 1]
# [1, 2]
# BFS from 0:
#
# Visit 0 → {0}
#
# Go to 1 → {0, 1}
#
# Go to 2 → {0, 1, 2}
#
# No way to reach 3 → disconnected ✅

