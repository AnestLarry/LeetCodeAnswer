#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#
# Note: I am compare the least at first,but it is very fool to sort the list again and again ,this solution though is based on the top voted Solution and use less memory

# Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

# Note:

# The number of elements initialized in nums1 and nums2 are m and n respectively.
# You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
# Example:

# Input:
# nums1 = [1,2,3,0,0,0], m = 3
# nums2 = [2,5,6],       n = 3

# Output: [1,2,2,3,5,6]
# √ Accepted
#   √ 59/59 cases passed (36 ms)
#   √ Your runtime beats 91.86 % of python3 submissions
#   √ Your memory usage beats 39.68 % of python3 submissions (13.2 MB)
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        end = len(nums1)-1
        m,n=m-1,n-1
        while m >=0 and n >= 0 :
            if nums1[m] > nums2[n]:
                nums1[end]=nums1[m]
                m-=1
            else:
                nums1[end]=nums2[n]
                n-=1
            end-=1
        if m<0:
            nums1[:n+1] = nums2[:n+1]
