# https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

# Postorder always ends with the root node.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not postorder or not inorder:
            return None
        root = TreeNode(postorder[-1])
        index = inorder.index(postorder[-1])
        # Build right subtree first (since postorder is Left -> Right -> Root)
        root.right = self.buildTree(inorder[index + 1:], postorder[index:-1])

        # Then build left subtree
        root.left = self.buildTree(inorder[:index], postorder[:index])
        return root

