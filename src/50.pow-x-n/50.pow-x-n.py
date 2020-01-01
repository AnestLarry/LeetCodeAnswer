#
# @lc app=leetcode id=50 lang=python3
#
# [50] Pow(x, n)
#
# Implement pow(x, n), which calculates x raised to the power n (xn).

# Example 1:

# Input: 2.00000, 10
# Output: 1024.00000
# Example 2:

# Input: 2.10000, 3
# Output: 9.26100
# Example 3:

# Input: 2.00000, -2
# Output: 0.25000
# Explanation: 2-2 = 1/22 = 1/4 = 0.25
# Note:

# -100.0 < x < 100.0
# n is a 32-bit signed integer, within the range [−231, 231 − 1]


class Solution:
    def myPow(self, x: float, n: int) -> float:
        # Accepted
        # 304/304 cases passed (24 ms)
        # Your runtime beats 99.43 % of python3 submissions
        # Your memory usage beats 99.51 % of python3 submissions (12.7 MB)
        m = n < 0
        p = 1.0
        while n != 0:
            if (n & 1) == 1:
                p *= x
            x *= x
            n = int(n/2)
        return 1/p if m else p

    def myPow2(self, x: float, n: int) -> float:
        # Accepted
        # 304/304 cases passed (24 ms)
        # Your runtime beats 99.43 % of python3 submissions
        # Your memory usage beats 99.51 % of python3 submissions (12.7 MB)
        return x**n
