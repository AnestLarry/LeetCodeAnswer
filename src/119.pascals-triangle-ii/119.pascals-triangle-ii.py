#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
# Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

# Note that the row index starts from 0.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 3
# Output: [1,3,3,1]
# Follow up:

# Could you optimize your algorithm to use only O(k) extra space?

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        # Accepted
        # 34/34 cases passed (28 ms)
        # Your runtime beats 91.7 % of python3 submissions
        # Your memory usage beats 23.12 % of python3 submissions (13.4 MB)
        res = [1]*(rowIndex + 1)
        for i in range(1, rowIndex+1):
            for j in range((rowIndex-i)+1, rowIndex):
                res[j] += res[j+1]
        return res

    def getRow2(self, rowIndex: int) -> List[int]:
        # Accepted
        # 34/34 cases passed (36 ms)
        # Your runtime beats 55.97 % of python3 submissions
        # Your memory usage beats 22.95 % of python3 submissions (13.4 MB)
        pascal = [1]*(rowIndex + 1)
        for i in range(2, rowIndex+1):
            for j in range(i-1, 0, -1):
                pascal[j] += pascal[j-1]
        return pascal
