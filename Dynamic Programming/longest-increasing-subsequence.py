from typing import List

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        length = [1] * n
        print(length)

        for i in range(1, n):
            for j in range(i):
                if nums[j] < nums[i]:
                    length[i] = max(length[i], length[j] + 1)

        return max(length)

# Sample input
nums = [10, 9, 2, 5, 3, 7, 101, 18]

solution = Solution()

print("Length of Longest Increasing Subsequence:", solution.lengthOfLIS(nums))
