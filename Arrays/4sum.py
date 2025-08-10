# https://www.youtube.com/watch?v=EYeR-_1NRlQ
# https://leetcode.com/problems/4sum/


from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res, quad = [], []

        def kSum(k, start, target):
            if k != 2:
                for i in range(start, len(nums) - k + 1):
                    if i > start and nums[i] == nums[i - 1]:
                        continue
                    quad.append(nums[i])
                    kSum(k - 1, i + 1, target - nums[i])
                    quad.pop()
                return

            # base case: 2Sum problem
            l, r = start, len(nums) - 1
            while l < r:
                curr = nums[l] + nums[r]
                if curr < target:
                    l += 1
                elif curr > target:
                    r -= 1
                else:
                    res.append(quad + [nums[l], nums[r]])
                    l += 1
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

        kSum(4, 0, target)
        return res
