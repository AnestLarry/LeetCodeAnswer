#
# @lc app=leetcode id=167 lang=python3
#
# [167] Two Sum II - Input array is sorted
#
# Note : It is a sorted list.

# Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

# The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

# Note:

# Your returned answers (both index1 and index2) are not zero-based.
# You may assume that each input would have exactly one solution and you may not use the same element twice.
# Example:

# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
# √ Accepted
#   √ 17/17 cases passed (40 ms)
#   √ Your runtime beats 82.93 % of python3 submissions
#   √ Your memory usage beats 23.55 % of python3 submissions (13.7 MB)
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = len(numbers)
        if l<3:
            return [1,2]
        i,j = 0,len(numbers)-1
        while i<j:
            r=numbers[i]+numbers[j]
            if r==target:
                return [i+1,j+1]
            elif r>target:
                j-=1
            else:
                i+=1
        return []
