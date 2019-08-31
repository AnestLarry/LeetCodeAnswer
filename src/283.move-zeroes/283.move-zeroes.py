#
# @lc app=leetcode id=283 lang=python3
#
# [283] Move Zeroes
#
# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Example:

# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # √ Accepted
        #   √ 21/21 cases passed (60 ms)
        #   √ Your runtime beats 62.85 % of python3 submissions
        #   √ Your memory usage beats 5.97 % of python3 submissions (15.1 MB)
        l,i = len(nums),0
        if l>1:
            n=0
            while i < l:
                if nums[i] != 0:
                    nums[n],nums[i] = nums[i],nums[n]
                    n+=1
                i+=1
    
    def moveZeroes2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # √ Accepted
        #     √ 21/21 cases passed (56 ms)
        #     √ Your runtime beats 84.72 % of python3 submissions
        #     √ Your memory usage beats 5.97 % of python3 submissions (15.1 MB)
        l,i = len(nums),0
        if l>1:
            n=0
            while i < l:
                if nums[i] != 0 :
                    if i != n:
                        nums[n] ^= nums[i]
                        nums[i] ^= nums[n]
                        nums[n] ^= nums[i]
                    n+=1
                i+=1
