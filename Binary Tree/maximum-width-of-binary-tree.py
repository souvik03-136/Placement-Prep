# https://leetcode.com/problems/maximum-width-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Sample tree construction for input: [1,3,2,5,3,null,9]
# Corresponding tree:
#         1
#       /   \
#      3     2
#     / \     \
#    5   3     9

root = TreeNode(1)
root.left = TreeNode(3)
root.right = TreeNode(2)
root.left.left = TreeNode(5)
root.left.right = TreeNode(3)
root.right.left = None
root.right.right = TreeNode(9)


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:

        if not root:
            return 0

        queue = [(root, 0)]  # store (node, index)
        result = []
        length = 0

        while queue:
            queue_length = len(queue)
            level = []

            for i in range(queue_length):
                node, index = queue.pop(0)

                level.append(index)

                if node.left:
                    queue.append((node.left, index * 2))
                if node.right:
                    queue.append((node.right, index * 2 + 1))

            result.append(level)

            width = level[0] + 1
            if width > length:
                length = width

        return length









# Instantiate and print output
s = Solution()
output = s.widthOfBinaryTree(root)
print(output)
