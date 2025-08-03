# https://leetcode.com/problems/valid-parentheses/



class Solution:
    def isValid(self, s: str) -> bool:

        l = []
        j = -1

        for i in s:
            if i in "({[":
                l.append(i)
                j += 1
            elif j >= 0 and i == ")" and l[j] == "(":
                del l[j]
                j -= 1
            elif j >= 0 and i == "}" and l[j] == "{":
                del l[j]
                j -= 1
            elif j >= 0 and i == "]" and l[j] == "[":
                del l[j]
                j -= 1
            else:
                return False
        return len(l) == 0
