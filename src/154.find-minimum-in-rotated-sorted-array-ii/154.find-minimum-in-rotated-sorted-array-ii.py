#
# @lc app=leetcode id=154 lang=python3
#
# [154] Find Minimum in Rotated Sorted Array II
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# The array may contain duplicates.

# Example 1:

# Input: [1,3,5]
# Output: 1
# Example 2:

# Input: [2,2,2,0,1]
# Output: 0
# Note:

# This is a follow up problem to Find Minimum in Rotated Sorted Array.
# Would allow duplicates affect the run-time complexity? How and why?


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Accepted
        # 192/192 cases passed (36 ms)
        # Your runtime beats 90.33 % of python3 submissions
        # Your memory usage beats 33.33 % of python3 submissions (13.7 MB)
        l: int = len(nums)
        if l < 2:
            return nums[0]
        last, i = l-1, l-2
        while i != -1 and nums[i] <= nums[last]:
            if nums[i >> 1] < nums[last]:
                last = i >> 1
                i = last-1
            else:
                last, i = i, i-1
        return nums[last]
