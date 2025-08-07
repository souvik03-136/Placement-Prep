# https://leetcode.com/problems/house-robber-ii/


class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])

        def rob_linear(houses):
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(dp[i - 1], dp[i - 2] + houses[i])
            return dp[-1]

        # Case 1: Exclude the last house
        money1 = rob_linear(nums[:-1])
        # Case 2: Exclude the first house
        money2 = rob_linear(nums[1:])

        return max(money1, money2)
