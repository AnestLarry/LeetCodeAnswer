#
# @lc app=leetcode id=153 lang=python3
#
# [153] Find Minimum in Rotated Sorted Array
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

# Find the minimum element.

# You may assume no duplicate exists in the array.

# Example 1:

# Input: [3,4,5,1,2]
# Output: 1
# Example 2:

# Input: [4,5,6,7,0,1,2]
# Output: 0


class Solution:
    def findMin(self, nums: List[int]) -> int:
        # Accepted
        # 146/146 cases passed (28 ms)
        # Your runtime beats 99.29 % of python3 submissions
        # Your memory usage beats 6.67 % of python3 submissions (13.8 MB)
        l: int = len(nums)
        if l < 2:
            return nums[0]
        last, i = l-1, l-2
        while i != -1 and nums[i] <= nums[last]:
            if nums[i >> 1] < nums[last]:
                i = (i >> 1)-1
                last = i+1
            else:
                last, i = i, i-1
        return nums[last]

    def findMin2(self, nums: List[int]) -> int:
        # Accepted
        # 146/146 cases passed (40 ms)
        # Your runtime beats 69.59 % of python3 submissions
        # Your memory usage beats 6.67 % of python3 submissions (13.7 MB)
        return min(nums)
