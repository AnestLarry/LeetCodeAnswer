#
# @lc app=leetcode.cn id=136 lang=python3
#
# [136] Single Number
#
# Given a non-empty array of integers, every element appears twice except for one. Find that single one.

# Note:

# Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

# Example 1:

# Input: [2,2,1]
# Output: 1
# Example 2:

# Input: [4,1,2,1,2]
# Output: 4
# @lc code=start


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Accepted
        # 16/16 cases passed (88 ms)
        # Your runtime beats 93.34 % of python3 submissions
        # Your memory usage beats 44.67 % of python3 submissions (15.6 MB)
        r = 0
        for i in (j for j in nums if j):
            r ^= i
        return r

    def singleNumber2(self, nums: List[int]) -> int:
        # Accepted
        # 16/16 cases passed (92 ms)
        # Your runtime beats 89.1 % of python3 submissions
        # Your memory usage beats 45.02 % of python3 submissions (15.5 MB)
        return 2*sum(set(nums))-sum(nums)


# @lc code=end
