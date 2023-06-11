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


class Solution:
    def countPrimes(self, n: int) -> int:
        # Accepted
        # 20/20 cases passed (144 ms)
        # Your runtime beats 82.93 % of python3 submissions
        # Your memory usage beats 23.51 % of python3 submissions (36.9 MB)
        if n <= 2:
            return 0
        res = [True] * n
        res[0] = res[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if res[i]:
                # res[i*i:n:i] = [False] * ((n - i*i - 1) // i + 1)
                res[i*i:n:i] = [False] * ((n - i*i - 1) // i + 1)
        return sum(res)
