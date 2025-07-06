# https://leetcode.com/problems/intersection-of-two-linked-lists/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodes1 = []
        nodes2 = []

        while headA:
            nodes1.append(headA)
            headA = headA.next
        while headB:
            nodes2.append(headB)
            headB = headB.next

        res = None
        if len(nodes1) < len(nodes2):
            for i in range(1, len(nodes1)+1):
                if nodes1[-i] is nodes2[-i]:
                    res = nodes1[-i]
                else:
                    break
        else:
            for i in range(1, len(nodes2)+1):
                if nodes2[-i] is nodes1[-i]:
                    res = nodes2[-i]
                else:
                    break

        return res
