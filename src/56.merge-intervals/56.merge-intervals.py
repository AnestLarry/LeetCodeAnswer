#
# @lc app=leetcode id=56 lang=python3
#
# [56] Merge Intervals
#
# √ Accepted
#   √ 169/169 cases passed (100 ms)
#   √ Your runtime beats 75.63 % of python3 submissions
#   √ Your memory usage beats 6.52 % of python3 submissions (16 MB)
# Given a collection of intervals, merge all overlapping intervals.

# Example 1:

# Input: [[1,3],[2,6],[8,10],[15,18]]
# Output: [[1,6],[8,10],[15,18]]
# Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# Example 2:

# Input: [[1,4],[4,5]]
# Output: [[1,5]]
# Explanation: Intervals [1,4] and [4,5] are considered overlapping.
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
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
