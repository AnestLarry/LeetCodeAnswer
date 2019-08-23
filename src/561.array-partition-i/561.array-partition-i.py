#
# @lc app=leetcode id=561 lang=python3
#
# [561] Array Partition I
#
# √ Accepted
#   √ 81/81 cases passed (324 ms)
#   √ Your runtime beats 87.3 % of python3 submissions
#   √ Your memory usage beats 6.06 % of python3 submissions (16.4 MB)
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()
        sum,l=0,len(nums)
        for i in (nums[x] for x in range(0,l,2)):
            sum+=i
        return sum

