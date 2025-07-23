# https://leetcode.com/problems/trapping-rain-water/
# https://www.youtube.com/watch?v=ZI2z5pq0TqA
class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)

        # Step 1: Precompute max to the right for each position
        max_right = [0] * n
        max_right[n - 1] = height[n - 1]
        for i in range(n - 2, -1, -1):
            max_right[i] = max(height[i], max_right[i + 1])

        # Step 2: Traverse from left to right and calculate trapped water
        water_trap = 0
        max_left = height[0]

        for i in range(1, n - 1):
            max_left = max(max_left, height[i])
            min_height = min(max_left, max_right[i])
            if min_height > height[i]:
                water_trap += min_height - height[i]

        return water_trap
