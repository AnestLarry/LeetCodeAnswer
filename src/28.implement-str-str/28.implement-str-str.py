#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # √ Accepted
        #   √ 74/74 cases passed (32 ms)
        #   √ Your runtime beats 94.29 % of python3 submissions
        #   √ Your memory usage beats 12.31 % of python3 submissions (14 MB)
        if not needle:
            return 0
        nl = len(needle)
        for i in range(0,len(haystack)-nl+1):
            if haystack[i:i+nl] == needle:
                return i
        return -1
