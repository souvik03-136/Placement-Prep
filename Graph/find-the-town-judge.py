# https://leetcode.com/problems/find-the-town-judge/


class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        l = []
        for u, v in trust:
            l.append(v)
        c = []
        for i in range(1, n + 1):
            if l.count(i) == n - 1:
                c.append(i)
        for u, v in trust:
            if u in c:
                c.remove(u)
        if len(c) == 1:
            return c[0]
        else:
            return -1
