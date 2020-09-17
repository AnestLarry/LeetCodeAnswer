#
# @lc app=leetcode id=202 lang=python3
#
# [202] Happy Number
#
# Write an algorithm to determine if a number is "happy".

# A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

# Example:

# Input: 19
# Output: true
# Explanation:
# 12 + 92 = 82
# 82 + 22 = 68
# 62 + 82 = 100
# 12 + 02 + 02 = 1


class Solution:
    def isHappy(self, n: int) -> bool:
        # Accepted
        # 401/401 cases passed (32 ms)
        # Your runtime beats 99.46 % of python3 submissions
        # Your memory usage beats 76.66 % of python3 submissions (13.6 MB)
        repeat = set()
        repeat.add(n)
        while n != 1:
            nn = 0
            while n > 0:
                d = n % 10
                nn += d * d
                n = int(n / 10)
            if nn in repeat:
                return False
            else:
                repeat.add(nn)
            n = nn
        return True
