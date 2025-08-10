# https://leetcode.com/problems/merge-intervals/



intervals = [[1,3],[2,6],[8,10],[15,18]]


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        i = 1
        while i < len(intervals):
            if intervals[i][0] <= intervals[i - 1][1]:
                intervals[i - 1][1] = max(intervals[i - 1][1], intervals[i][1])
                del intervals[i]
            else:
                i += 1
        return intervals