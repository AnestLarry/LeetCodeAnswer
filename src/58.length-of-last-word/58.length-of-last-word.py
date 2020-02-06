#
# @lc app=leetcode id=58 lang=python3
#
# [58] Length of Last Word
#
# Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

# If the last word does not exist, return 0.

# Note: A word is defined as a character sequence consists of non-space characters only.

# Example:

# Input: "Hello World"
# Output: 5


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Accepted
        # 59/59 cases passed (24 ms)
        # Your runtime beats 97.88 % of python3 submissions
        # Your memory usage beats 53.63 % of python3 submissions (13.2 MB)
        r, res = len(s)-1, 0
        while r > -1 and s[r] == " ":
            r -= 1
        while r > -1 and s[r] != " ":
            r -= 1
            res += 1
        return res

    def lengthOfLastWord2(self, s: str) -> int:
        # Accepted
        # 59/59 cases passed (24 ms)
        # Your runtime beats 97.88 % of python3 submissions
        # Your memory usage beats 53.68 % of python3 submissions (13.1 MB)
        s = s.strip()
        l = len(s)
        if self.checkword(s):
            if " " in s:
                return l - s.rindex(" ") - 1
            else:
                return l
        return 0

    def checkword(self, n):
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in n:
                return True
        return False
