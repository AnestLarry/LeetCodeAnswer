#
# @lc app=leetcode id=240 lang=python3
#
# [240] Search a 2D Matrix II
#
# Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

# Integers in each row are sorted in ascending from left to right.
# Integers in each column are sorted in ascending from top to bottom.
# Example:

# Consider the following matrix:

# [
#   [1,   4,  7, 11, 15],
#   [2,   5,  8, 12, 19],
#   [3,   6,  9, 16, 22],
#   [10, 13, 14, 17, 24],
#   [18, 21, 23, 26, 30]
# ]
# Given target = 5, return true.

# Given target = 20, return false.
class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        # √ Accepted
        # √ 129/129 cases passed (44 ms)
        # √ Your runtime beats 79.95 % of python3 submissions
        # √ Your memory usage beats 5 % of python3 submissions (18.5 MB)
        """
        if matrix:
            ml,l=len(matrix),len(matrix[0])
            for i in range(ml):
                for j in range(l):
                    if matrix[i][j]==target:
                        return True
            return False
        return False
        """
        # √ Accepted
        # √ 129/129 cases passed (40 ms)
        # √ Your runtime beats 92.08 % of python3 submissions
        # √ Your memory usage beats 5 % of python3 submissions (18.7 MB)
        for i in matrix:
            if i.count(target)>0:
                return True
        return False
