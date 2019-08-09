#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?
# √ Accepted
#   √ 275/275 cases passed (56 ms)
#   √ Your runtime beats 96.88 % of python3 submissions
#   √ Your memory usage beats 5.72 % of python3 submissions (14.1 MB)
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        if not nums:
            return False
        l=len(nums)
        if target >= nums[0]:
            last=i=0
            while i<l and nums[i]>=nums[last]:
                if nums[i]==target:
                    return True
                last=i
                i+=1
            return False
        else:
            last=i=l-1
            while i>0 and nums[i]<=nums[last]:
                if nums[i] == target:
                    return True
                last=i
                i-=1
            return False
            

