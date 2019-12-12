#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#
# There are two sorted arrays nums1 and nums2 of size m and n respectively.

# Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

# You may assume nums1 and nums2 cannot be both empty.

# Example 1:

# nums1 = [1, 3]
# nums2 = [2]

# The median is 2.0
# Example 2:

# nums1 = [1, 2]
# nums2 = [3, 4]

# The median is (2 + 3)/2 = 2.5


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Accepted
        # 2085/2085 cases passed (100 ms)
        # Your runtime beats 99.34 % of python3 submissions
        # Your memory usage beats 99.43 % of python3 submissions (12.8 MB)
        nums = []
        i, j, il, jl = 0, 0, len(nums1), len(nums2)
        while i < il and j < jl:
            if nums1[i] < nums2[j]:
                nums += [nums1[i]]
                i += 1
            else:
                nums += [nums2[j]]
                j += 1
        if i < il:
            nums += nums1[i:]
        else:
            nums += nums2[j:]
        l = len(nums)
        if l % 2 == 0:
            return (nums[int(l/2)]+nums[int(l/2-1)])/2
        else:
            return nums[int(l/2)]
