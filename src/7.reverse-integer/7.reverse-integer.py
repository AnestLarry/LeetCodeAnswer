#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
#  Given a 32-bit signed integer, reverse digits of an integer.

# Example 1:

# Input: 123
# Output: 321
# Example 2:

# Input: -123
# Output: -321
# Example 3:

# Input: 120
# Output: 21
# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.


class Solution:
    def reverse(self, x: int) -> int:
        # Accepted
        # 1032/1032 cases passed (32 ms)
        # Your runtime beats 98.53 % of python3 submissions
        # Your memory usage beats 99.88 % of python3 submissions (12.6 MB)
        smollerzero = False
        s, p, seq, res = str(x), 0, 0, 0
        l = len(s)
        while p < l:
            if s[p] == "-":
                p += 1
                smollerzero = True
                continue
            res += int(s[p])*10**seq
            p, seq = p+1, seq+1
        if smollerzero:
            res *= -1
        if res > 2147483647 or res <= -2147483648:
            return 0
        else:
            return res

    def reverse2(self, x: int) -> int:
        # Accepted
        # 1032/1032 cases passed (32 ms)
        # Your runtime beats 98.53 % of python3 submissions
        # Your memory usage beats 99.88 % of python3 submissions (12.7 MB)
        smollerzero = False
        s, res = str(x), ""
        if s[0] == "-":
            smollerzero = True
            s = s[1:]
        l = len(s)-1
        while l > -1:
            res += s[l]
            l -= 1
        if smollerzero:
            res = int(res)*-1
        else:
            res = int(res)
        if res > 2147483647 or res <= -2147483648:
            return 0
        else:
            return res
