#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
# Given an unsorted integer array, find the smallest missing positive integer.

# Example 1:

# Input: [1,2,0]
# Output: 3
# Example 2:

# Input: [3,4,-1,1]
# Output: 2
# Example 3:

# Input: [7,8,9,11,12]
# Output: 1
# Note:

# Your algorithm should run in O(n) time and uses constant extra space.

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Accepted
        # 165/165 cases passed (32 ms)
        # Your runtime beats 97.5 % of python3 submissions
        # Your memory usage beats 100 % of python3 submissions (12.8 MB)
        nums = [x for x in nums if x > 0]
        if nums:
            for i in range(1, max(nums)+2):
                if not i in nums:
                    return i
        else:
            return 1

# @lc code=end
