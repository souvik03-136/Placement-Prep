# https://leetcode.com/problems/is-graph-bipartite/

# https://chatgpt.com/c/685da00a-4f40-8010-b368-3f1f9e397873

from typing import List

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        color = [-1] * n  # -1 means uncolored
        print(color)

        def dfs(node, c):
            color[node] = c  # Color the current node
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    if not dfs(neighbor, 1 - c):  # Try to color with opposite
                        return False
                elif color[neighbor] == color[node]:
                    return False  # Same color on both ends
            return True

        for i in range(n):
            if color[i] == -1:  # Not visited yet
                if not dfs(i, 0):
                    return False

        return True
graph = [[1,2,3],[0,2],[0,1,3],[0,2]]

print(Solution().isBipartite(graph))