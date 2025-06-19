# https://takeuforward.org/interviews/strivers-sde-sheet-top-coding-interview-problems



# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        l1 = []
        l2 = []

        def insertinl1(node):
            if not node:
                l1.append(None)
                return
            l1.append(node.val)
            insertinl1(node.left)
            insertinl1(node.right)

        def insertinl2(node):
            if not node:
                l2.append(None)
                return
            l2.append(node.val)
            insertinl2(node.right)
            insertinl2(node.left)

        insertinl1(root.left)
        insertinl2(root.right)

        return l1 == l2