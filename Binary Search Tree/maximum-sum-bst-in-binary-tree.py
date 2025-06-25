# https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxSumBST(self, root):
        self.ans = 0

        def helper(node):
            if not node:
                return True, 0, float('inf'), float('-inf')  # isBST, sum, min, max

            left_is_bst, left_sum, left_min, left_max = helper(node.left)
            right_is_bst, right_sum, right_min, right_max = helper(node.right)

            # Check if current tree is a BST
            if left_is_bst and right_is_bst and node.val > left_max and node.val < right_min:
                total_sum = left_sum + right_sum + node.val
                self.ans = max(self.ans, total_sum)
                min_val = min(node.val, left_min)
                max_val = max(node.val, right_max)
                return True, total_sum, min_val, max_val
            else:
                return False, 0, 0, 0

        helper(root)
        return self.ans


# BRUTE FORCE


class Solution:
    def maxSumBST(self, root):
        self.max_sum = 0

        def isBST(node, min_val, max_val):
            if not node:
                return True
            if node.val <= min_val or node.val >= max_val:
                return False
            return isBST(node.left, min_val, node.val) and isBST(node.right, node.val, max_val)

        def sumTree(node):
            if not node:
                return 0
            return node.val + sumTree(node.left) + sumTree(node.right)

        def traverse(node):
            if not node:
                return
            if isBST(node, float('-inf'), float('inf')):
                total = sumTree(node)
                self.max_sum = max(self.max_sum, total)
            traverse(node.left)
            traverse(node.right)

        traverse(root)
        return self.max_sum
