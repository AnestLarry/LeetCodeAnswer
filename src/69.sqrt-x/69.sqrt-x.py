#
# @lc app=leetcode id=69 lang=python3
#
# [69] Sqrt(x)
#
# Implement int sqrt(int x).

# Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

# Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

# Example 1:

# Input: 4
# Output: 2
# Example 2:

# Input: 8
# Output: 2
# Explanation: The square root of 8 is 2.82842..., and since
#              the decimal part is truncated, 2 is returned.


class Solution:
    def mySqrt(self, x: int) -> int:
        # Accepted
        # 1017/1017 cases passed (32 ms)
        # Your runtime beats 94.74 % of python3 submissions
        # Your memory usage beats 53.22 % of python3 submissions (13 MB)
        if x in (0, 1):
            return x
        guess, temp = x * (2/x), 0
        while True:
            guess = (guess+x/guess)/2
            if temp == int(guess):
                break
            else:
                temp = int(guess)
        return int(guess)

    def mySqrt2(self, x: int) -> int:
        # Accepted
        # 1017/1017 cases passed (24 ms)
        # Your runtime beats 99.82 % of python3 submissions
        # Your memory usage beats 53.22 % of python3 submissions (13 MB)
        return int(x**0.5)
