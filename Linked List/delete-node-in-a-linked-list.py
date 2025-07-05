# https://leetcode.com/problems/delete-node-in-a-linked-list/submissions/1687710953/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next