#
# @lc app=leetcode id=53 lang=python3
#
# [53] Maximum Subarray
#

# @lc code=start
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

# Example:

# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
# Follow up:

# If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.


class Solution:
    def maxSubArray1(self, nums: List[int]) -> int:
        # Accepted
        # 202/202 cases passed (68 ms)
        # Your runtime beats 98.63 % of python3 submissions
        # Your memory usage beats 73.5 % of python3 submissions (13.6 MB)
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        bl = maxnum = nums[0]
        for i in range(1, nums_len):
            bl = bl+nums[i] if bl > 0 else nums[i]
            if bl > maxnum:
                maxnum = bl
        return maxnum

    def maxSubArray(self, nums: List[int]) -> int:
        # Accepted
        # 202/202 cases passed (64 ms)
        # Your runtime beats 99.54 % of python3 submissions
        # Your memory usage beats 40.49 % of python3 submissions (13.7 MB)
        nums_len = len(nums)
        if nums_len == 1:
            return nums[0]
        bl = [nums[0]]+[0]*(nums_len-1)
        for i in range(1, nums_len):
            bl[i] = bl[i-1]+nums[i] if bl[i-1] > 0 else nums[i]
        return max(bl)
# @lc code=end
