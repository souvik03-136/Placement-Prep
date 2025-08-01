# https://leetcode.com/problems/find-center-of-star-graph/description/
from collections import Counter

# OPTIMAL

from collections import Counter
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        l = []
        for u, v in edges:
            l.append(u)
            l.append(v)
        freq = Counter(l)
        sorted_lst = sorted(l, key=lambda x: (-freq[x], x))
        return sorted_lst[0]

# OR

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        l = []
        for u, v in edges:
            l.append(u)
            l.append(v)

        freq = Counter(l)
        max_freq = 1
        s = max(l) + 1

        for i in freq:
            if freq[i] > max_freq:
                max_freq = freq[i]
                s = i
        return s

#BRUTE FORCE
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        l = []
        for u, v in edges:
            l.append(u)
            l.append(v)
        max_freq = 1
        l1 = set(l)
        s = max(l)+1
        for i in l1:
             if l.count(i)>max_freq:
                 max_freq = l.count(i)
                 s = i
        return s

