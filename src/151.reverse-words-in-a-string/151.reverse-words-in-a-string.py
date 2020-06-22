#
# @lc app=leetcode id=151 lang=python3
#
# [151] Reverse Words in a String
#
# Given an input string, reverse the string word by word.


# Example 1:

# Input: "the sky is blue"
# Output: "blue is sky the"
# Example 2:

# Input: "  hello world!  "
# Output: "world! hello"
# Explanation: Your reversed string should not contain leading or trailing spaces.
# Example 3:

# Input: "a good   example"
# Output: "example good a"
# Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


# Note:

# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.


# Follow up:

# For C programmers, try to solve it in-place in O(1) extra space.


class Solution:
    def reverseWords(self, s: str) -> str:
        # Accepted
        # 25/25 cases passed (32 ms)
        # Your runtime beats 97.42 % of python3 submissions
        # Your memory usage beats 10 % of python3 submissions (13.6 MB)        s = s.strip()
        sl = s.split()
        sl.reverse()
        return " ".join([x for x in sl])

    def reverseWords2(self, s: str) -> str:
        # Accepted
        # 25/25 cases passed (40 ms)
        # Your runtime beats 76.26 % of python3 submissions
        # Your memory usage beats 10 % of python3 submissions (13.9 MB)
        import re
        sl = re.compile("[^ ]+").findall(s)
        return " ".join([sl[x] for x in range(len(sl)-1, -1, -1)])
