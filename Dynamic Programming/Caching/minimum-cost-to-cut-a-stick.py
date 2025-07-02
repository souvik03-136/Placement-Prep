# https://leetcode.com/problems/minimum-cost-to-cut-a-stick/
# https://www.youtube.com/watch?v=EVxTO5I0d7w

class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.append(0)
        cuts.append(n)
        cuts.sort()

        dp = {}

        def dfs(l, r):
            if r - l == 1:
                return 0
            if (l, r) in dp:
                return dp[(l, r)]
            res = float("inf")
            for c in cuts:
                if l < c < r:
                    res = min(res, (r - l) + dfs(l, c) + dfs(c, r))
            dp[(l, r)] = 0 if res == float("inf") else res
            return dp[(l, r)]

        return dfs(0, n)
