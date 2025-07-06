#https://leetcode.com/problems/rotate-list/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        arr = []
        temp = head
        while temp:
            arr.append(temp.val)
            temp = temp.next

        if not arr:
            return head

        k = k % len(arr)
        arr = arr[-k:] + arr[:-k]

        temp = head
        for val in arr:
            temp.val = val
            temp = temp.next

        return head