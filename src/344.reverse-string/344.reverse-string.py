#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#
# Write a function that reverses a string. The input string is given as an array of characters char[].

# Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

# You may assume all the characters consist of printable ascii characters.

# Example 1:

# Input: ["h","e","l","l","o"]
# Output: ["o","l","l","e","h"]
# Example 2:

# Input: ["H","a","n","n","a","h"]
# Output: ["h","a","n","n","a","H"]
# @lc code=start
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        # Accepted
        # 478/478 cases passed (228 ms)
        # Your runtime beats 83.72 % of python3 submissions
        # Your memory usage beats 46.51 % of python3 submissions (17.7 MB)
        l,r = 0,len(s)-1
        while l<r:
            s[l],s[r] = s[r],s[l]
            l,r=l+1,r-1
            
        
# @lc code=end

