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


class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Accepted
        # 989/989 cases passed (36 ms)
        # Your runtime beats 90.81 % of python3 submissions
        # Your memory usage beats 99.52 % of python3 submissions (12.7 MB)
        ind = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        result = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                result += i
                i <<= 1
                temp <<= 1
        if not ind:
            result *= -1
        if result > (1 << 31)-1:
            return (1 << 31)-1
        elif result < -1 << 31:
            return -1 << 31
        else:
            return result

    def divide2(self, dividend: int, divisor: int) -> int:
        # Accepted
        # 989/989 cases passed (32 ms)
        # Your runtime beats 96.74 % of python3 submissions
        # Your memory usage beats 99.52 % of python3 submissions (12.7 MB)
        result = int(dividend/divisor)
        if result > (1 << 31)-1:
            return (1 << 31)-1
        elif result < -1 << 31:
            return -1 << 31
        else:
            return result
