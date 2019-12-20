#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#
# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # Accepted
        # 313/313 cases passed (848 ms)
        # Your runtime beats 84.65 % of python3 submissions
        # Your memory usage beats 23.46 % of python3 submissions (17.1 MB)        nums.sort()
        l = len(nums)
        if l == 3 and sum(nums) == 0:
            return [nums]
        res = []
        for i in range(l):
            last = l-1
            j = i+1
            if i != 0 and nums[i] == nums[i-1]:
                continue
            while j < last:
                s = nums[i]+nums[j]+nums[last]
                if s < 0:
                    j += 1
                elif s > 0:
                    last -= 1
                else:
                    res += [[nums[i], nums[j], nums[last]]]
                    j += 1
                    last -= 1
                    while j != (i+1) and nums[j] == nums[j-1] and j < last:
                        j += 1
                    while last != (l-1) and nums[last] == nums[last+1] and last > j:
                        last -= 1
        return res
