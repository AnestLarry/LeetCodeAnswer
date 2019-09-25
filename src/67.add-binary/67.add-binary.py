#
# @lc app=leetcode id=67 lang=python3
#
# [67] Add Binary
#
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        # √ Accepted
        #   √ 294/294 cases passed (36 ms)
        #   √ Your runtime beats 89.96 % of python3 submissions
        #   √ Your memory usage beats 5.41 % of python3 submissions (13.9 MB)
        s = int(a,2) + int(b,2)
        return str(bin(s))[2:]

