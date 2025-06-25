# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []

        def dfs(node, depth):
            if not node:
                return

            # If we're at a new depth level not yet in result, add a new list
            if len(result) == depth:
                result.append([])

            # Append the current node's value to its level
            result[depth].append(node.val)

            # Recur for left and right children
            dfs(node.left, depth + 1)
            dfs(node.right, depth + 1)

        dfs(root, 0)
        return result
