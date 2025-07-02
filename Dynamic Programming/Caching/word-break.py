# https://leetcode.com/problems/word-break/
# https://www.youtube.com/watch?v=Sx9NNgInc3A

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s)+1)
        dp[len(s)] = True
        for i in range(len(s)-1,-1,-1):
            for w in wordDict:
                if (i+len(w)) <=len(s) and s[i: i+len(w)] == w: #this means there are enough charater in s for us to compare
                    dp[i] = dp[i+len(w)]
                if dp[i]:
                    break
        return dp[0]