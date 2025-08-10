# https://leetcode.com/problems/insert-interval/


from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # We'll build a new list for results
        result = []
        inserted = False

        for interval in intervals:
            u, v = interval
            if v < newInterval[0]:
                # Current interval ends before newInterval starts, add it as is
                result.append(interval)
            elif u > newInterval[1]:
                # Current interval starts after newInterval ends
                if not inserted:
                    result.append(newInterval)
                    inserted = True
                result.append(interval)
            else:
                # Overlapping intervals: merge with newInterval
                newInterval[0] = min(newInterval[0], u)
                newInterval[1] = max(newInterval[1], v)

        # If newInterval wasn't inserted, add it at the end
        if not inserted:
            result.append(newInterval)

        return result
