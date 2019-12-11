#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#
# Given an array of integers, return indices of the two numbers such that they add up to a specific target.

# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# Example:

# Given nums = [2, 7, 11, 15], target = 9,

# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Accepted
        # 29/29 cases passed (60 ms)
        # Your runtime beats 93.87 % of python3 submissions
        # Your memory usage beats 53.21 % of python3 submissions (14.1 MB)
        m = {}
        i = 0
        while i < len(nums):
            if nums[i] not in m.keys():
                m[target - nums[i]] = i
            else:
                return m[nums[i]], i
            i += 1
        return -1, -1
