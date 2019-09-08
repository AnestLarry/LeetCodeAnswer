#
# @lc app=leetcode id=204 lang=python3
#
# [204] Count Primes
#
# Count the number of prime numbers less than a non-negative number, n.

# Example:

# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
# √ Accepted
#   √ 20/20 cases passed (804 ms)
#   √ Your runtime beats 37.07 % of python3 submissions
#   √ Your memory usage beats 79.31 % of python3 submissions (25.3 MB)

class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3:
            return 0
        r = [True]*n
        for i in range(2,n):
            if r[i]:
                for j in range(2,(n-1)//i+1):
                    r[i*j]= False
        return sum(r)-2
