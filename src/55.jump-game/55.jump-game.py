#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        k = 0
        l = len(nums)
        i = 0
        while i<=k:
            t = i+nums[i]
            k = k if k>t else t
            if k>=l-1:
                return True
            i+=1
        return False
# @lc code=end
