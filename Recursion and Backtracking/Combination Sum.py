# https://leetcode.com/problems/combination-sum/description/
# https://www.youtube.com/watch?v=GBKI9VSKdGg

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        def backtrack(start, path, total):
            if total == target:
                result.append(path[:])
                return
            if total > target:
                return

            for i in range(start, len(candidates)):
                # pick the same number again, so we pass i, not i+1
                path.append(candidates[i])
                backtrack(i, path, total + candidates[i])
                path.pop()  # backtrack

        backtrack(0, [], 0)
        return result

