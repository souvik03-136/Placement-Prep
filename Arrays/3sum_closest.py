# https://leetcode.com/problems/3sum-closest/description/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = [nums[0], nums[1], nums[2]]
        nums.sort()
        for i, a in enumerate(nums):
            l, r = i + 1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]

                if abs(target - threeSum) < abs(target - sum(res)):
                    res[0], res[1], res[2] = a, nums[l], nums[r]

                if threeSum > target:
                    r -= 1
                elif threeSum < target:
                    l += 1
                else:
                    return threeSum
        return sum(res)
