#
# @lc app=leetcode id=278 lang=python3
#
# [278] First Bad Version
#
# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):
# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.

# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.

# You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# Example:

# Given n = 5, and version = 4 is the first bad version.

# call isBadVersion(3) -> false
# call isBadVersion(5) -> true
# call isBadVersion(4) -> true

# Then 4 is the first bad version. 
class Solution:
    def firstBadVersion(self, n:int ) -> int:
        """
        :type n: int
        :rtype: int
        """
        # √ Accepted
        #   √ 22/22 cases passed (28 ms)
        #   √ Your runtime beats 97.96 % of python3 submissions
        #   √ Your memory usage beats 6.9 % of python3 submissions (13.7 MB)
        l,m,r = 0,0,n
        while l<=r:
            m=(l+r)//2
            if isBadVersion(m):
                r=m-1
            else:
                l=m+1
        return l
