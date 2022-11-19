#
# @lc app=leetcode.cn id=1732 lang=python3
#
# [1732] Find the Highest Altitude
#
# There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

# You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

# @lc code=start
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        # Accepted
        # 80/80 cases passed (24 ms)
        # Your runtime beats 99.61 % of python3 submissions
        # Your memory usage beats 76.65 % of python3 submissions (14.9 MB)
        res = 0
        cur = 0
        for i in gain:
            cur += i
            if cur > res:
                res = cur
        return res
# @lc code=end
