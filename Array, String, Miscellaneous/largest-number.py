# https://leetcode.com/problems/largest-number/description/


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        final = ""
        if len(set(nums)) == 1 and nums[0] == 0:
            return "0"
        else:
            for i in range(len(nums)):
                for j in range(len(nums) - i - 1):
                    if str(nums[j]) + str(nums[j + 1]) < str(nums[j + 1]) + str(nums[j]):
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
            for k in nums:
                final += str(k)
            return final

