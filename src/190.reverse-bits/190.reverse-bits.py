#
# @lc app=leetcode.cn id=190 lang=python3
#
# [190] Reverse Bits
#
# Accepted
# 600/600 cases passed (36 ms)
# Your runtime beats 93.26 % of python3 submissions
# Your memory usage beats 20.64 % of python3 submissions (13.7 MB)

# @lc code=start
class Solution:
    def reverseBits(self, n: int) -> int:
        m = 0
        res = 0
        while res < 32:
            m = m << 1 | n >> res & 1
            res += 1
        return m
        # @lc code=end
