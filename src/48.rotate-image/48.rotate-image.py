#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#
# You are given an n x n 2D matrix representing an image.

# Rotate the image by 90 degrees (clockwise).

# Note:

# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

# Example 1:

# Given input matrix =
# [
#   [1,2,3],
#   [4,5,6],
#   [7,8,9]
# ],

# rotate the input matrix in-place such that it becomes:
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
# ]
# Example 2:

# Given input matrix =
# [
#   [ 5, 1, 9,11],
#   [ 2, 4, 8,10],
#   [13, 3, 6, 7],
#   [15,14,12,16]
# ],

# rotate the input matrix in-place such that it becomes:
# [
#   [15,13, 2, 5],
#   [14, 3, 4, 1],
#   [12, 6, 8, 9],
#   [16, 7,10,11]
# ]
# Note : https://docs.python.org/3.7/library/functions.html#zip


class Solution:
    def rotate(self, matrix):
        # Accepted
        # 21/21 cases passed (36 ms)
        # Your runtime beats 95.22 % of python3 submissions
        # Your memory usage beats 100 % of python3 submissions (12.8 MB)
        matrix.reverse()
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def rotate2(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Accepted
        # 21/21 cases passed (36 ms)
        # Your runtime beats 95.22 % of python3 submissions
        # Your memory usage beats 100 % of python3 submissions (12.7 MB)
        matrix[:] = zip(*matrix[::-1])
