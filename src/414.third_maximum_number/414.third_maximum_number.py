#
# @lc app=leetcode id=414 lang=python3
#
# [414] Third Maximum Number
#
# @lc code=start
# Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

# Example 1:
# Input: [3, 2, 1]

# Output: 1

# Explanation: The third maximum is 1.
# Example 2:
# Input: [1, 2]

# Output: 2

# Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
# Example 3:
# Input: [2, 2, 3, 1]

# Output: 1

# Explanation: Note that the third maximum here means the third maximum distinct number.
# Both numbers with value 2 are both considered as second maximum.


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        # Accepted
        # 26 / 26 test cases passed. (56 ms)
        # Your runtime beats 81.25 % of python3 submissions
        # Your memory usage beats 30.77% % of python3 submissions (12.8 MB)
        nums = list(set(nums))
        l = len(nums)
        if l < 4:
            return max(nums) if l < 3 else min(nums)
        maxs = [min(nums)]*3
        for i in nums:
            if i > maxs[0]:
                maxs[0], maxs[1], maxs[2] = (i, maxs[0], maxs[1]) if not i in maxs else (
                    maxs[0], maxs[1], maxs[2])
            elif i > maxs[1]:
                maxs[1], maxs[2] = (i, maxs[1]) if not i in maxs else (
                    maxs[1], maxs[2])
            elif i > maxs[2]:
                maxs[2] = i if not i in maxs else maxs[2]
        return maxs[2]
# @lc code=end
