# https://leetcode.com/problems/longest-substring-without-repeating-characters/submissions/1642269566/

s = "abcabcbb"
length = 0
i = 0
j = len(s)

while i < j:
    s1 = ''
    k = i
    while k < j and s[k] not in s1:
        s1 += s[k]
        k += 1
    if len(s1) > length:
        length = len(s1)
    i += 1

print(length)
