# https://leetcode.com/problems/longest-consecutive-sequence/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_set = set(nums)
        longest = 0

        for n in num_set:
            if n - 1 not in num_set:  # start of a sequence
                length = 1
                while n + length in num_set:
                    length += 1
                longest = max(longest, length)

        return longest
