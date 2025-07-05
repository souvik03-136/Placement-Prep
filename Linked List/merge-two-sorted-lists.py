# https://leetcode.com/problems/merge-two-sorted-lists/submissions/1687698552/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []

        # Collect all nodes from list1 and list2
        while list1:
            nodes.append(list1)
            list1 = list1.next
        while list2:
            nodes.append(list2)
            list2 = list2.next

        # Sort the nodes based on their values
        nodes.sort(key=lambda node: node.val)

        # Re-link nodes
        for i in range(len(nodes) - 1):
            nodes[i].next = nodes[i + 1]

        if nodes:
            nodes[-1].next = None
            return nodes[0]
        else:
            return None
