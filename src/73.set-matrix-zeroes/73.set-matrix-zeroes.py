#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#
# Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

# Example 1:

# Input: 
# [
#   [1,1,1],
#   [1,0,1],
#   [1,1,1]
# ]
# Output: 
# [
#   [1,0,1],
#   [0,0,0],
#   [1,0,1]
# ]
# Example 2:

# Input: 
# [
#   [0,1,2,0],
#   [3,4,5,2],
#   [1,3,1,5]
# ]
# Output: 
# [
#   [0,0,0,0],
#   [0,4,5,0],
#   [0,3,1,0]
# ]
# Follow up:

# A straight forward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?
# √ Accepted
#   √ 159/159 cases passed (148 ms)
#   √ Your runtime beats 5.66 % of python3 submissions
#   √ Your memory usage beats 5.25 % of python3 submissions (14.6 MB)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ml,l=len(matrix),len(matrix[0])
        z=[]
        for i in range(ml):
            if matrix[i].count(0) > 0:
                for j in range(l):
                    if matrix[i][j]==0:
                        z+=[(i,j)]
        if z != []:
            for i in z:
                for j in range(l):
                    matrix[i[0]][j]=0
                for j in range(ml):
                    matrix[j][i[1]]=0
