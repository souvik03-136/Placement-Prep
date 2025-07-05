# https://leetcode.com/problems/remove-nth-node-from-end-of-list/submissions/1687706575/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        nodes = []

        # Step 1: Store all nodes in a list
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next

        # Step 2: If the head itself needs to be removed
        if n == len(nodes):
            return head.next

        # Step 3: Remove the nth node from the end
        nodes[-n - 1].next = nodes[-n + 1] if n != 1 else None

        # Step 4: Return the head of the new list
        return nodes[0]