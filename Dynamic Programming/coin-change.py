#https://leetcode.com/problems/coin-change/description/

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1) #0 .... amt and [amount + 1] is for storiing max val, we can also store inf
        dp[0] = 0
        print(dp)

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])  # 1 comes from the current coin c
        print(dp)
        if dp[amount] != amount + 1: # not equal to the default val we gave / inf..
            return dp[amount]
        else:
            return -1
