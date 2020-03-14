#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
# Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note:

# The same word in the dictionary may be reused multiple times in the segmentation.
# You may assume the dictionary does not contain duplicate words.
# Example 1:

# Input: s = "leetcode", wordDict = ["leet", "code"]
# Output: true
# Explanation: Return true because "leetcode" can be segmented as "leet code".
# Example 2:

# Input: s = "applepenapple", wordDict = ["apple", "pen"]
# Output: true
# Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
#              Note that you are allowed to reuse a dictionary word.
# Example 3:

# Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
# Output: false

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Accepted
        # 36/36 cases passed (32 ms)
        # Your runtime beats 98.38 % of python3 submissions
        # Your memory usage beats 6.76 % of python3 submissions (13.6 MB)
        if not wordDict:
            return not s
        l = len(s)
        bl = [False] * (l + 1)
        bl[0] = True
        for i in range(1, l + 1):
            for j in range(i - 1, -1, -1):
                if bl[j] and s[j:i] in wordDict:
                    bl[i] = True
                    break
        return bl[-1]
