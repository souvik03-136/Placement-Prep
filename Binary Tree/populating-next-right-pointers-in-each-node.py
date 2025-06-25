# https://leetcode.com/problems/populating-next-right-pointers-in-each-node/

# https://www.youtube.com/watch?v=U4hFQCa1Cq0
"""
# Definition for a Node."""
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:
            return None

        cur = root

        while cur and cur.left:
            next_level = cur.left
            while cur:
                cur.left.next = cur.right
                if cur.next:
                    cur.right.next = cur.next.left
                cur = cur.next
            cur = next_level

        return root


