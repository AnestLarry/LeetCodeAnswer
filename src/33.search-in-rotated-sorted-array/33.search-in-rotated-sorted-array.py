#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

# You are given a target value to search. If found in the array return its index, otherwise return -1.

# You may assume no duplicate exists in the array.

# Your algorithm's runtime complexity must be in the order of O(log n).

# Example 1:

# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:

# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# √ Accepted
#   √ 196/196 cases passed (48 ms)
#   √ Your runtime beats 78.41 % of python3 submissions
#   √ Your memory usage beats 5 % of python3 submissions (14.1 MB)
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=len(nums)
        if l <1:
            return -1
        elif l<2:
            if nums[0]==target:
                return 0
            else:
                return -1
        num,n=self.mysort(nums,l)
        left,right=0,l-1
        result=-1
        while left<=right:
            mid = int((left+right)/2)
            if num[mid] == target:
                result=mid+n
                if result>l-1:
                    if n!=0:
                        return result-l
                return result
            if num[mid] < target:
                left=mid+1
            else:
                right=mid-1
        return result

    def mysort(self,nums,length):
        head= nums[0]
        for i in range(1,length):
            if nums[i]<head:
                return nums[i:]+nums[:i],i
        return nums,0

