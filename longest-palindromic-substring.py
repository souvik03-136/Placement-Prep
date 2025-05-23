# https://leetcode.com/problems/longest-palindromic-substring/submissions/1642305689/

s = "babad"
length = 0
longest = ""

for i in range(len(s)):
    for j in range(i + 1, len(s) + 1):
        print(i,j)
        sub = s[i:j]
        if sub == sub[::-1]:
            if len(sub) > length:
                length = len(sub)
                longest = sub

print(longest)
