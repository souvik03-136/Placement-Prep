# https://leetcode.com/problems/3sum/
# https://www.youtube.com/watch?v=jzZsG8n2R9A


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i, a in enumerate(nums):  # Iterating through index and value
            if i > 0 and a == nums[i - 1]:  # That meeans it is the same value as before and we dont want to reuse it so just continue iterating
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0:
                    r -= 1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a, nums[l], nums[r]])
                    l += 1
                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
        return res
