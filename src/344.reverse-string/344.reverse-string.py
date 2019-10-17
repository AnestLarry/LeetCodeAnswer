#
# @lc app=leetcode id=344 lang=python3
#
# [344] Reverse String
#

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

