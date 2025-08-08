# https://leetcode.com/problems/clone-graph/
# https://www.youtube.com/watch?v=mQeF6bN8hMk&t=134s
# https://www.youtube.com/watch?v=mQeF6bN8hMk&t=134s

"""
# Definition for a Node."""
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val


from typing import Optional


class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        OldToNew = {} #hash map


        def dfs(node):
            if node in OldToNew: # we already made a clone of it
                return OldToNew[node]
            copy = Node(node.val)
            OldToNew[node] = copy #old node is the node and the new node is the copy
            for neighbour in node.neighbours:
                copy.neighbours.append(dfs(neighbour))
            return copy
        return dfs(node) if node else None




'''BRUTE FORCE'''


class Node:
    def __init__(self, val, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors else []


class Solution:
    def cloneGraph(self, node):
        if not node:
            return None

        visited = {}

        def dfs(n):
            if n in visited:
                return visited[n]

            copy = Node(n.val)
            visited[n] = copy

            for nei in n.neighbors:
                copy.neighbors.append(dfs(nei))

            return copy

        return dfs(node)
