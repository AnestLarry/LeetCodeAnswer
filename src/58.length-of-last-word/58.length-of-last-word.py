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
# √ Accepted
#   √ 59/59 cases passed (24 ms)
#   √ Your runtime beats 99.68 % of python3 submissions
#   √ Your memory usage beats 14.23 % of python3 submissions (13.3 MB)
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        l=len(s)
        if self.checkword(s):
            try:
                return l- s.rindex(" ") -1
            except:
                return l
        print("not in low")
        return 0
        
    def checkword(self,n):
        for i in "abcdefghijklmnopqrstuvwxyz":
            if i in n:
                return True
        return False
