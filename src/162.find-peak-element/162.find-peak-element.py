#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#
# A peak element is an element that is greater than its neighbors.

# Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

# The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

# You may imagine that nums[-1] = nums[n] = -∞.

# Example 1:

# Input: nums = [1,2,3,1]
# Output: 2
# Explanation: 3 is a peak element and your function should return the index number 2.
# Example 2:

# Input: nums = [1,2,1,3,5,6,4]
# Output: 1 or 5 
# Explanation: Your function can return either index number 1 where the peak element is 2, 
#              or index number 5 where the peak element is 6.
# Note:

# Your solution should be in logarithmic complexity.

class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # O(n)
        # √ Accepted
        #   √ 59/59 cases passed (56 ms)
        #   √ Your runtime beats 55.81 % of python3 submissions
        #   √ Your memory usage beats 5.88 % of python3 submissions (14.1 MB)
        l=len(nums)
        if l<2:
            return 0
        i = 1
        while i < l:
            if nums[i] <nums[i-1]:
                return i-1
            i+=1
        return i-1

    def findPeakElement2(self, nums:list) -> int:
        h = 0
        t = len(nums)
        l = t
        i = 0
        #m = 0
        while l > 1:
            if l < 3:
                if nums[h]>nums[h+1]:
                    i = h
                else:
                    i = h+1
                l = 1
            else:
                m = int((t-h)/2)+h
                if nums[m]>nums[m-1]:
                    h = m
                else:
                    t = m+1
                l = t-h
        return i

    def findPeakElement3(self, nums:list) -> int:
        return self.fpe(nums, 0, len(nums), len(nums))

    def fpe(self, q, h, t, l):
        if l < 2:
            return h
        elif l < 3:
            if q[h]>q[h+1]:
                return h
            else:
                return h+1
        else:
            m = int((t-h)/2)+h
            if q[m]>q[m-1]:
                return self.fpe(q, m, t, t-m)
            else:
                return self.fpe(q, h, m, m-h)
