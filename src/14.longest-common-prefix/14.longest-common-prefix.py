#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

# Example 1:

# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:

# All given inputs are in lowercase letters a-z.
# √ Accepted
#   √ 118/118 cases passed (36 ms)
#   √ Your runtime beats 81.86 % of python3 submissions
#   √ Your memory usage beats 62.52 % of python3 submissions (13.2 MB)
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res=""
        for i in zip(*strs):
            if len(set(i))>1:
                break
            res+=i[0]
        return res
