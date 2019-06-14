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
# √ Accepted
#   √ 304/304 cases passed (1320 ms)
#   √ Your runtime beats 7.41 % of python3 submissions
#   √ Your memory usage beats 72.96 % of python3 submissions (13.1 MB)
class Solution:
    def myPow(self, x: float, n: int) -> float:
        #return x**n
        res=1
        if x == 1:
            return 1
        elif x == -1 :
            if n%2 == 0:
                return 1
            return -1
        if n < 0 :
            x=1/x
            n*=-1
        while n>0 and round(res,5)!=0:
            res*=x
            n-=1
        return round(res,5)
