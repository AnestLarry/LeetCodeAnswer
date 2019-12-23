#
# @lc app=leetcode id=28 lang=python3
#
# [28] Implement strStr()
#
#  Implement strStr().

# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

# Example 1:

# Input: haystack = "hello", needle = "ll"
# Output: 2
# Example 2:

# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
# Clarification:

# What should we return when needle is an empty string? This is a great question to ask during an interview.

# For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        # Accepted
        # 74/74 cases passed (28 ms)
        # Your runtime beats 98.22 % of python3 submissions
        # Your memory usage beats 99.53 % of python3 submissions (12.8 MB)
        if not needle:
            return 0
        nl = len(needle)
        for i in range(len(haystack)-nl+1):
            if haystack[i:i+nl] == needle:
                return i
        return -1
