#
# @lc app=leetcode id=81 lang=python3
#
# [81] Search in Rotated Sorted Array II
#
# Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

# (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

# You are given a target value to search. If found in the array return true, otherwise return false.

# Example 1:

# Input: nums = [2,5,6,0,0,1,2], target = 0
# Output: true
# Example 2:

# Input: nums = [2,5,6,0,0,1,2], target = 3
# Output: false
# Follow up:

# This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
# Would this affect the run-time complexity? How and why?


class Solution:
    def search(self, nums, target):
        # Accepted
        # 275/275 cases passed (36 ms)
        # Your runtime beats 97.8 % of python3 submissions
        # Your memory usage beats 30.54 % of python3 submissions (13.6 MB)
        l, r = 0, len(nums)-1
        while l <= r:
            mid = l + ((r-l) >> 1)
            if nums[mid] == target:
                return True
            while l < mid and nums[l] == nums[mid]:  # tricky part
                l += 1
            # the first half is ordered
            if nums[l] <= nums[mid]:
                # target is in the first half
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            # the second half is ordered
            else:
                # target is in the second half
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1
        return False

    def search2(self, nums: List[int], target: int) -> bool:
        # Accepted
        # 275/275 cases passed (64 ms)
        # Your runtime beats 50.1 % of python3 submissions
        # Your memory usage beats 35.17 % of python3 submissions (13.9 MB)class Solution:
        if not nums:
            return False
        l = len(nums)
        if target >= nums[0]:
            last = i = 0
            while i < l and nums[i] >= nums[last]:
                if nums[i] == target:
                    return True
                last = i
                i += 1
            return False
        else:
            last = i = l-1
            while i > 0 and nums[i] <= nums[last]:
                if nums[i] == target:
                    return True
                last = i
                i -= 1
            return False
