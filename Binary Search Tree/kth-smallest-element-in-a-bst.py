# https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = []

        def insert(node):
            if not node:
                return
            l.append(node.val)
            insert(node.left)
            insert(node.right)

        insert(root)

        l.sort()
        return l[k - 1]
