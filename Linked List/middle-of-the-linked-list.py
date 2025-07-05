# https://leetcode.com/problems/middle-of-the-linked-list/description/

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        nodes = []
        while head:
            nodes.append(head)
            head = head.next
        return nodes[len(nodes) // 2]

# OR GPT LOGIC

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow

# Easy Explanation:
# slow moves 1 step at a time.
# fast moves 2 steps at a time.
# When fast reaches the end, slow will be at the middle.
# Example:
# Input:
# 1 -> 2 -> 3 -> 4 -> 5
# Output:
# 3 -> 4 -> 5
#
# Input:
# 1 -> 2 -> 3 -> 4 -> 5 -> 6
# Output:
# 4 -> 5 -> 6 (second middle when even number of nodes)

