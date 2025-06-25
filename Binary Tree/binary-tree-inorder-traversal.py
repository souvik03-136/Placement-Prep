# https://leetcode.com/problems/binary-tree-inorder-traversal/description/


# Recursive
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def inorder(root):
            if root is None:
                return
            else:
                inorder(root.left)
                result.append(root.val)
                inorder(root.right)
        inorder(root)
        return result

# Iterative

