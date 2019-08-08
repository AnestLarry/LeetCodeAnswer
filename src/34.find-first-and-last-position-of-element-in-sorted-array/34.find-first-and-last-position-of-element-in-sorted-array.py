#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#
# Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

# Your algorithm's runtime complexity must be in the order of O(log n).

# If the target is not found in the array, return [-1, -1].

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# √ Accepted
#   √ 88/88 cases passed (88 ms)
#   √ Your runtime beats 99.6 % of python3 submissions
#   √ Your memory usage beats 5.36 % of python3 submissions (15 MB)
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        first,last,l = -1,-1,len(nums)
        if not nums:
            return [first,last]
        for i in range(l):
            if nums[i]<target:
                continue
            elif nums[i]==target:
                first=last=i
                for j in range(i,l):
                    if nums[j]==nums[i]:
                        last=j
                    else:
                        return [first,last]
                return [first,last]
            else:
                return [first,last]
        return [first,last]
