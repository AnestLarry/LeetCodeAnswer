#
# @lc app=leetcode id=287 lang=python3
#
# [287] Find the Duplicate Number
#
# Given an array nums containing n + 1 integers where each integer is between 1 and n (inclusive), prove that at least one duplicate number must exist. Assume that there is only one duplicate number, find the duplicate one.

# Example 1:

# Input: [1,3,4,2,2]
# Output: 2
# Example 2:

# Input: [3,1,3,4,2]
# Output: 3
# Note:

# You must not modify the array (assume the array is read only).
# You must use only constant, O(1) extra space.
# Your runtime complexity should be less than O(n2).
# There is only one duplicate number in the array, but it could be repeated more than once.

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # √ Accepted
        #   √ 53/53 cases passed (72 ms)
        #   √ Your runtime beats 94.07 % of python3 submissions
        #   √ Your memory usage beats 7.14 % of python3 submissions (16.1 MB)
        slow = fast = finder = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                while finder != slow:
                    finder = nums[finder]
                    slow = nums[slow]
                return finder
