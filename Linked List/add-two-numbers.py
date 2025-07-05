# https://leetcode.com/problems/add-two-numbers/submissions/1687710060/


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # Step 1: Read digits into lists
        num1 = []
        num2 = []

        while l1:
            num1.append(l1.val)
            l1 = l1.next
        while l2:
            num2.append(l2.val)
            l2 = l2.next

        # Step 2: Add digit by digit
        i = 0
        carry = 0
        result = []

        while i < max(len(num1), len(num2)) or carry:
            val1 = num1[i] if i < len(num1) else 0
            val2 = num2[i] if i < len(num2) else 0

            total = val1 + val2 + carry
            carry = total // 10
            result.append(total % 10)
            i += 1

        # Step 3: Make linked list from result list
        dummy = ListNode()
        current = dummy

        for digit in result:
            current.next = ListNode(digit)
            current = current.next

        return dummy.next
