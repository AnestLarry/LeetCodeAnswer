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
# √ Accepted
#   √ 11509/11509 cases passed (88 ms)
#   √ Your runtime beats 52.57 % of python3 submissions
#   √ Your memory usage beats 61.88 % of python3 submissions (13.3 MB)
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0:
            return False
        elif x<10:
            return True
        r,rx = 0,x
        while x >0:
            r,x=r*10 + x%10,int(x/10)
        if r ==rx :
            return True
        return False
