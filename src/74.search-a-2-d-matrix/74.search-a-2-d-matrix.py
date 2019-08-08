#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted from left to right.
# The first integer of each row is greater than the last integer of the previous row.
# Example 1:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 3
# Output: true
# Example 2:

# Input:
# matrix = [
#   [1,   3,  5,  7],
#   [10, 11, 16, 20],
#   [23, 30, 34, 50]
# ]
# target = 13
# Output: false
# √ Accepted
#   √ 136/136 cases passed (72 ms)
#   √ Your runtime beats 94.26 % of python3 submissions
#   √ Your memory usage beats 5.88 % of python3 submissions (15.8 MB)
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:
            return False
        ll=len(matrix[0])
        if ll <1:
            return False
        for i in range(len(matrix)):
            if matrix[i][-1]<target:
                continue
            else:
                for j in range(ll):
                    if matrix[i][j]==target:
                        return True
                return False
        return False

