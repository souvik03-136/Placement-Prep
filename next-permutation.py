# https://leetcode.com/problems/next-permutation/




nums = [1,2,3]

if nums == sorted(nums, reverse=True):
    nums.sort()
else:
    for i in range(len(nums) - 2, -1, -1):
        if nums[i] < nums[i + 1]:
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    nums[i + 1:] = reversed(nums[i + 1:])

print(nums)