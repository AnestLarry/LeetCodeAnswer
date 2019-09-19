#
# @lc app=leetcode id=268 lang=python3
#
# [268] Missing Number
#
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # √ Accepted
        #   √ 122/122 cases passed (156 ms)
        #   √ Your runtime beats 68.15 % of python3 submissions
        #   √ Your memory usage beats 6.45 % of python3 submissions (15.7 MB)
        s = set(nums)
        for i in range(len(s)+1):
            if not i in s:
                return i
