#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
# Given two binary strings, return their sum (also a binary string).

# The input strings are both non-empty and contains only characters 1 or 0.

# Example 1:

# Input: a = "11", b = "1"
# Output: "100"
# Example 2:

# Input: a = "1010", b = "1011"
# Output: "10101"


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # Accepted
        # 294/294 cases passed (28 ms)
        # Your runtime beats 96.5 % of python3 submissions
        # Your memory usage beats 54.94 % of python3 submissions (13.2 MB)
        if len(a) > len(b):
            b = "0"*(len(a)-len(b)) + b
        else:
            a = "0"*(len(b)-len(a)) + a
        res, i, flag = "", len(a)-1, False
        while -1 < i:
            if a[i] == b[i] == "0":
                res += "1" if flag else "0"
                flag = False
            elif a[i] == b[i] == "1":
                res += "1" if flag else "0"
                flag = True
            else:
                res += "0" if flag else "1"
            i -= 1
        if flag:
            res += "1"
        return res[::-1]

    def addBinary2(self, a: str, b: str) -> str:
        # Accepted
        # 294/294 cases passed (32 ms)
        # Your runtime beats 90.33 % of python3 submissions
        # Your memory usage beats 55.05 % of python3 submissions (13 MB)        s = int(a,2) + int(b,2)
        s = int(a, 2) + int(b, 2)
        return str(bin(s))[2:]
