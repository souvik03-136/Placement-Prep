# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m = len(text1)
        n = len(text2)

        dp = []
        for i in range(m + 1):
            row = []
            for j in range(n + 1):
                row.append(0)
            dp.append(row)


        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if text1[i - 1] == text2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        print(dp)

        return dp[m][n]

text1 = "abcde"
text2 = "ace"

sol = Solution()
result = sol.longestCommonSubsequence(text1, text2)
print("Length of Longest Common Subsequence:", result)
