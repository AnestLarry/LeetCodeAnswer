#
# @lc app=leetcode id=57 lang=python3
#
# [57] Insert Interval
#
# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

# You may assume that the intervals were initially sorted according to their start times.

# Example 1:

# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:

# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
# NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.


class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Accepted
        # 154/154 cases passed (88 ms)
        # Your runtime beats 86.94 % of python3 submissions
        # Your memory usage beats 50.59 % of python3 submissions (16.7 MB)
        flag = False
        for i in range(len(intervals)):
            if intervals[i][0] > newInterval[0]:
                intervals.insert(i, newInterval)
                flag = True
                break
        if not flag:
            intervals.append(newInterval)
        return self.merge(intervals)

    def insert2(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Accepted
        # 154/154 cases passed (80 ms)
        # Your runtime beats 95.39 % of python3 submissions
        # Your memory usage beats 50.59 % of python3 submissions (16.7 MB)
        intervals.append(newInterval)
        intervals.sort()
        return self.merge(intervals)

    def merge(self, intervals):
        out = []
        for i in sorted(intervals, key=lambda i: i[0]):
            if out and i[0] <= out[-1][1]:
                out[-1][1] = max(out[-1][1], i[1])
            else:
                out += i,
        return out
