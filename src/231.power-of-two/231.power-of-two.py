#
# @lc app=leetcode id=231 lang=python3
#
# [231] Power of Two
#

# @lc code=start
# Given an integer, write a function to determine if it is a power of two.

# Example 1:

# Input: 1
# Output: true
# Explanation: 20 = 1
# Example 2:

# Input: 16
# Output: true
# Explanation: 24 = 16
# Example 3:

# Input: 218
# Output: false


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # Accepted
        # 1108/1108 cases passed (36 ms)
        # Your runtime beats 83.78 % of python3 submissions
        # Your memory usage beats 9.52 % of python3 submissions (13.8 MB)
        return (n > 0) and (n & (n-1)) == 0

    def isPowerOfTwo2(self, n: int) -> bool:
        # Accepted
        # 1108/1108 cases passed (36 ms)
        # Your runtime beats 83.78 % of python3 submissions
        # Your memory usage beats 9.52 % of python3 submissions (14 MB)
        i = 1
        while i <= n:
            if i == n:
                return True
            i *= 2
        return False

    def isPowerOfTwo3(self, n: int) -> bool:
        # √ Accepted
        #   √ 1108/1108 cases passed (36 ms)
        #   √ Your runtime beats 79.02 % of python3 submissions
        #   √ Your memory usage beats 70.91 % of python3 submissions (13.2 MB)
        import math
        if n <= 0:
            return False
        elif n == 1:
            return True
        if n > 131072:
            n /= 65536
        m = math.log(n, 2)
        if m == math.floor(m):
            return True
        else:
            print(m, math.floor(m))
            return False
# @lc code=end
