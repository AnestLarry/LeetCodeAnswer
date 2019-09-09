#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# √ Accepted
#   √ 169/169 cases passed (100 ms)
#   √ Your runtime beats 75.63 % of python3 submissions
#   √ Your memory usage beats 6.52 % of python3 submissions (16 MB)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        i=0
        if len(intervals)==1:
            return intervals
        intervals.sort()
        while i < len(intervals)-1:
            if intervals[i][1] >= intervals[i+1][0]:
                if intervals[i][1] < intervals[i+1][1]:
                    intervals[i][1] = intervals.pop(i+1)[1]
                else:
                    del intervals[i+1]
            else:
                i+=1
        return intervals
