# https://leetcode.com/problems/find-if-path-exists-in-graph/

from typing import List

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = {}
        for u, v in edges:

            if u not in graph:
                graph[u] = []
            if v not in graph:
                graph[v] = []
            graph[u].append(v)
            graph[v].append(u)

        visited = set()
        queue = [source]

        while queue:
            node = queue.pop(0)
            if node == destination:
                return True
            if node in visited:
                continue
            visited.add(node)
            for neighbor in graph.get(node, []):
                if neighbor not in visited:
                    queue.append(neighbor)

        if destination in visited:
            return True
        else:
            return False



edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
n = 6
source = 0
destination = 5

sol = Solution()
print(sol.validPath(n, edges, source, destination))