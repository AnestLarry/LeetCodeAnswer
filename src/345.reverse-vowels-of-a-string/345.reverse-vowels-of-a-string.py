#
# @lc app=leetcode id=345 lang=python3
#
# [345] Reverse Vowels of a String
#

# @lc code=start


class Solution:
    def reverseVowels(self, s: str) -> str:
        # Accepted
        # 481/481 cases passed (68 ms)
        # Your runtime beats 43.67 % of python3 submissions
        # Your memory usage beats 6.67 % of python3 submissions (15 MB)
        vowwels, n, l, chars = ("a", "e", "i", "o", "u",
                                "A", "E", "I", "O", "U"), 0, len(s), []
        for i in s:
            if i in vowwels:
                chars += [i]
        s = list(s)
        if chars:
            while n < l:
                if s[n] in vowwels:
                    s[n] = chars.pop()
                n += 1
        return "".join(s)
# @lc code=end
