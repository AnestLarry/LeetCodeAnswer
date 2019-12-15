#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#
# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

# Example 1:

# Input: 121
# Output: true
# Example 2:

# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:

# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
# Follow up:

# Coud you solve it without converting the integer to a string?


class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Accepted
        # 11509/11509 cases passed (52 ms)
        # Your runtime beats 99.61 % of python3 submissions
        # Your memory usage beats 99.64 % of python3 submissions (12.7 MB)
        if x < 0:
            return False
        xs = str(x)
        l_xs = len(xs)
        left = []
        if l_xs % 2 != 0:
            left = xs[:l_xs//2+1]
        else:
            left = xs[:l_xs//2]
        right = xs[l_xs//2:]
        return left == right[::-1]

    def isPalindrome2(self, x: int) -> bool:
        # Accepted
        # 11509/11509 cases passed (72 ms)
        # Your runtime beats 83.15 % of python3 submissions
        # Your memory usage beats 99.64 % of python3 submissions (12.7 MB)
        if x < 0:
            return False
        elif x < 10:
            return True
        r, rx = 0, x
        while x > 0:
            r, x = r*10 + x % 10, int(x/10)
        if r == rx:
            return True
        return False
