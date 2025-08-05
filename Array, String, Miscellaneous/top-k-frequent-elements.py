# https://leetcode.com/problems/top-k-frequent-elements/description/

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        final = {}
        set1 = set(nums)
        for i in set1:
            final[i] = nums.count(i)

        sorted_items = sorted(final.items(), key=lambda item: item[1], reverse=True)
        return [item[0] for item in sorted_items[:k]]