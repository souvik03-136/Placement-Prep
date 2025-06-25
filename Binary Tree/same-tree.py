# https://leetcode.com/problems/same-tree/description/


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []
        def pushp(node):
            if not node:
                l1.append(None)
                return 0
            l1.append(node.val)
            pushp(node.left)
            pushp(node.right)
        def pushq(node):
            if not node:
                l2.append(None)
                return 0
            l2.append(node.val)
            pushq(node.left)
            pushq(node.right)
        pushp(p)
        pushq(q)
        if l1 == l2:
            return True
        else:
            return False



# Efficient
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q:
            return True
        if not p or not q:
            return False
        if p.val != q.val:
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)