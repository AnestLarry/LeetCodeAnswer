#
# @lc app=leetcode id=905 lang=python3
#
# [905] Sort Array By Parity
#
# Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

# You may return any answer array that satisfies this condition.

# Example 1:

# Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
 
# Note:

# 1 <= A.length <= 5000
# 0 <= A[i] <= 5000
# √ Accepted
#   √ 285/285 cases passed (96 ms)
#   √ Your runtime beats 55.05 % of python3 submissions
#   √ Your memory usage beats 5.19 % of python3 submissions (14.6 MB)

class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        return [x for x in A if x %2==0] + [y for y in A if y %2==1]

