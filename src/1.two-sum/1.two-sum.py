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
        i,j,l=0,1,len(nums)
        while  i <l:
            while j < l:
                if nums[i]+nums[j] == target:
                    return[i,j]
                j+=1
            i,j=i+1,i+2


