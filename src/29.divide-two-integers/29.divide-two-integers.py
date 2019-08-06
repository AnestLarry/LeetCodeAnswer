#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#
# Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

# Return the quotient after dividing dividend by divisor.

# The integer division should truncate toward zero.

# Example 1:

# Input: dividend = 10, divisor = 3
# Output: 3
# Example 2:

# Input: dividend = 7, divisor = -3
# Output: -2
# Note:
# Both dividend and divisor will be 32-bit signed integers.
# The divisor will never be 0.

# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.
# √ Accepted
#   √ 989/989 cases passed (36 ms)
#   √ Your runtime beats 87.98 % of python3 submissions
#   √ Your memory usage beats 5.62 % of python3 submissions (13.9 MB)
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        result=int(dividend/divisor)
        if result >2147483647:
            return 2147483647
        elif result <-2147483648:
            return -2147483648
        else:
            return result
