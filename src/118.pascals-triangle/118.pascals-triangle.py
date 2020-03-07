#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.


# In Pascal's triangle, each number is the sum of the two numbers directly above it.

# Example:

# Input: 5
# Output:
# [
#      [1],
#     [1,1],
#    [1,2,1],
#   [1,3,3,1],
#  [1,4,6,4,1]
# ]

class Solution:
    def generate1(self, numRows: int) -> List[List[int]]:
        # Accepted
        # 15/15 cases passed (28 ms)
        # Your runtime beats 90.21 % of python3 submissions
        # Your memory usage beats 32.78 % of python3 submissions (13.5 MB)
        base = [[1]]
        if numRows < 1:
            return []
        elif numRows == 1:
            return base
        numRows -= 1
        while numRows > 0:
            base.append(
                [1] +
                [base[-1][x]+base[-1][x+1] for x in range(len(base[-1]) - 1)]
                + [1]
            )
            numRows -= 1
        return base

    def generate(self, numRows):
        # Accepted
        # 15/15 cases passed (28 ms)
        # Your runtime beats 90.21 % of python3 submissions
        # Your memory usage beats 32.88 % of python3 submissions (13.1 MB)        pascal = [[1]*(i+1) for i in range(numRows)]
        pascal = [[1]*(i+1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
        return pascal
