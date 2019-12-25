#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#
# Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

# You may assume no duplicates in the array.

# Example 1:

# Input: [1,3,5,6], 5
# Output: 2
# Example 2:

# Input: [1,3,5,6], 2
# Output: 1
# Example 3:

# Input: [1,3,5,6], 7
# Output: 4
# Example 4:

# Input: [1,3,5,6], 0
# Output: 0


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Accepted
        # 62/62 cases passed (36 ms)
        # Your runtime beats 100 % of python3 submissions
        # Your memory usage beats 99.85 % of python3 submissions (13.4 MB)
        i = 0
        while i < len(nums):
            if nums[i] >= target:
                return i
            i += 1
        return len(nums)

    def searchInsert2(self, nums: List[int], target: int) -> int:
        # Accepted
        # 62/62 cases passed (44 ms)
        # Your runtime beats 99.84 % of python3 submissions
        # Your memory usage beats 99.95 % of python3 submissions (13.3 MB)
        left, right = 0, len(nums)-1
        while left <= right:
            mid = (left+right)//2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid+1
            else:
                right = mid-1
        return left
