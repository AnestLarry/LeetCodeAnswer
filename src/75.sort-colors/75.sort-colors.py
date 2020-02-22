#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

# Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

# Note: You are not suppose to use the library's sort function for this problem.

# Example:

# Input: [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
# Follow up:

# A rather straight forward solution is a two-pass algorithm using counting sort.
# First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
# Could you come up with a one-pass algorithm using only constant space?

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Accepted
        # 87/87 cases passed (32 ms)
        # Your runtime beats 86.65 % of python3 submissions
        # Your memory usage beats 46.36 % of python3 submissions (13.1 MB)
        l, r, c = 0, len(nums)-1, 0
        while c <= r:
            if nums[c] == 0:
                if nums[l] != nums[c]:
                    nums[c], nums[l] = nums[l], nums[c]
                c += 1
                l += 1
            elif nums[c] == 2:
                if nums[c] != nums[r]:
                    nums[c], nums[r] = nums[r], nums[c]
                r -= 1
            else:
                c += 1

    def sortColors2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Accepted
        # 87/87 cases passed (32 ms)
        # Your runtime beats 86.65 % of python3 submissions
        # Your memory usage beats 46.36 % of python3 submissions (13.1 MB)
        self.sortArray(nums)

    def sortArray(self, nums: List[int]) -> List[int]:
        # 912.Sort-an-array
        length = len(nums)
        if length < 2:
            return nums
        mid = length//2
        L, R = self.sortArray(nums[:mid]), self.sortArray(nums[mid:])

        i = j = 0
        il, jl = len(L), len(R)
        nums.clear()
        while i < il and j < jl:
            if L[i] < R[j]:
                nums.append(L[i])
                i += 1
            else:
                nums.append(R[j])
                j += 1
        if i < il:
            nums += L[i:]
        else:
            nums += R[j:]
        return nums
