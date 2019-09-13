#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        # √ Accepted
        #   √ 15/15 cases passed (32 ms)
        #   √ Your runtime beats 93.87 % of python3 submissions
        #   √ Your memory usage beats 7.14 % of python3 submissions (14 MB)
        base = [[1]]
        if numRows < 1:
            return []
        elif numRows ==1:
            return base
        numRows -=1
        while numRows > 0:
            base.append(
                 [1] + \
                 [ base[-1][x]+base[-1][x+1] for x in range(len(base[-1]) -1) ]     \
                 + [1] 
                 )
            numRows -= 1
        return base
