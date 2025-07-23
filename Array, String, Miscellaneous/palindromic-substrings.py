# https://leetcode.com/problems/palindromic-substrings/description/

class Solution:
    def countSubstrings(self, s: str) -> int:
        max1 = 0
        length = len(s)
        for i in range(length):
            for j in range(i, length):
                if s[i:j+1] == s[i:j+1][::-1]:
                    max1 += 1
        return max1
