# https://leetcode.com/problems/find-median-from-data-stream/
# https://www.youtube.com/watch?v=itmhHWaHupI


class MedianFinder:

    def __init__(self):
        self.nums = []

    def addNum(self, num: int) -> None:
        self.nums.append(num)

    def findMedian(self) -> float:
        self.nums.sort()
        n = len(self.nums)
        mid = n // 2
        if n % 2 == 0:
            return (self.nums[mid - 1] + self.nums[mid]) / 2
        else:
            return self.nums[mid]



# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()



'''OPTIMISED AS 
addNum() is O(1) (fast)

But findMedian() is O(n log n) due to sorting each time — very inefficient if you call findMedian() frequently'''



import heapq

class MedianFinder:

    def __init__(self):
        self.left = []  # Max-heap (invert values to use min-heap as max-heap)
        self.right = []  # Min-heap

    def addNum(self, num: int) -> None:
        # Step 1: Push to max-heap (left)
        heapq.heappush(self.left, -num)

        # Step 2: Balance - max from left should go to right
        heapq.heappush(self.right, -heapq.heappop(self.left))

        # Step 3: Maintain size property: left can have 1 extra
        if len(self.right) > len(self.left):
            heapq.heappush(self.left, -heapq.heappop(self.right))

    def findMedian(self) -> float:
        if len(self.left) > len(self.right):
            return -self.left[0]
        else:
            return (-self.left[0] + self.right[0]) / 2
