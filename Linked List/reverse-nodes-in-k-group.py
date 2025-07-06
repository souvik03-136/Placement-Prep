# https://leetcode.com/problems/reverse-nodes-in-k-group/
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        nodes = []
        temp = head
        while temp:
            nodes.append(temp)
            temp = temp.next

        for i in range(0, len(nodes) - (len(nodes) % k), k):
            for j in range(k // 2):
                nodes[i + j].val, nodes[i + k - 1 - j].val = nodes[i + k - 1 - j].val, nodes[i + j].val

        return head
