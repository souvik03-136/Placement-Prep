# https://leetcode.com/problems/maximum-product-subarray/description/

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        final_prod = nums[0]
        n = len(nums)

        for start in range(n):
            prod = 1
            for end in range(start, n):
                prod *= nums[end]
                final_prod = max(final_prod, prod)
                if nums[end] == 0:
                    break
        return final_prod



# USING DP
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1
        for n in nums:
            if n == 0:
                curMax, curMin = 1, 1
                continue
            temp = n * curMax
            curMax = max(n * curMin, n * curMax, n)
            curMin = min(n * curMin, temp, n)
            res = max(res, curMax)
        return res
