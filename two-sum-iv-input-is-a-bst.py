# https://leetcode.com/problems/two-sum-iv-input-is-a-bst/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        l = []
        def insert(node):
            if not node:
                return
            l.append(node.val)
            insert(node.left)
            insert(node.right)
        insert(root)
        ptr = 0

        for i in l:
            if (k-i) in l and l.index(i) != l.index(k-i):
                ptr = 1
        return ptr ==1


# OPTIMIZED
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        seen = set()

        def dfs(node):
            if not node:
                return False
            if k - node.val in seen:
                return True
            seen.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
