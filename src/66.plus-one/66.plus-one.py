#
# @lc app=leetcode id=66 lang=python3
#
# [66] Plus One
#
# Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

# The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

# You may assume the integer does not contain any leading zero, except the number 0 itself.

# Example 1:

# Input: [1,2,3]
# Output: [1,2,4]
# Explanation: The array represents the integer 123.
# Example 2:

# Input: [4,3,2,1]
# Output: [4,3,2,2]
# Explanation: The array represents the integer 4321.


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # Accepted
        # 109/109 cases passed (32 ms)
        # Your runtime beats 87.96 % of python3 submissions
        # Your memory usage beats 54.55 % of python3 submissions (13.3 MB)
        if digits == [0]:
            return [1]
        l = len(digits)-1
        return self.add(digits, l)

    def add(self, arr, p):
        if p < 0:
            return [1]+arr
        arr[p] += 1
        if arr[p] < 10:
            return arr
        else:
            arr[p] -= 10
            return self.add(arr, p-1)
