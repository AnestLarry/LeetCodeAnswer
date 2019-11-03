#
# @lc app=leetcode id=342 lang=python3
#
# [342] Power of Four
#

# @lc code=start
# Given an integer (signed 32 bits), write a function to check whether it is a power of 4.

# Example 1:

# Input: 16
# Output: true
# Example 2:

# Input: 5
# Output: false
# Follow up: Could you solve it without loops/recursion?

class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        # 0x55555555's binary representation is :1010101010101010101010101010101
        # 1010101010101010101010101010101=4^15 + 4^14 + ... + 4^2 + 4^1 + 4^0,here '^' means power
        # if num & 0x55555555 not equals 0,meaning that there is at least one bit in num's binary representation
        # Accepted
        # 1060/1060 cases passed (40 ms)
        # Your runtime beats 54.24 % of python3 submissions
        # Your memory usage beats 8.7 % of python3 submissions (13.9 MB)
        return num > 0 and (num & (num-1)) == 0 and (num & 0x55555555) != 0
# @lc code=end
