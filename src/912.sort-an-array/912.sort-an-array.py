#
# @lc app=leetcode id=912 lang=python3
#
# [912] Sort an Array
#
# Given an array of integers nums, sort the array in ascending order.

# Example 1:

# Input: [5,2,3,1]
# Output: [1,2,3,5]
# Example 2:

# Input: [5,1,1,2,0,0]
# Output: [0,0,1,1,2,5]

# Note:

# 1 <= A.length <= 10000
# -50000 <= A[i] <= 50000
class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        # √ Accepted
        #   √ 10/10 cases passed (344 ms)
        #   √ Your runtime beats 40 % of python3 submissions
        #   √ Your memory usage beats 64.29 % of python3 submissions (19.6 MB)
        length=len(nums)
        if length <2:
            return nums
        notsorted = False
        for i in range(1,length):
            if nums[i] < nums[i-1]:
                notsorted=True
                break
        if not notsorted:
            return nums
        mid = length//2
        L,R = self.sortArray(nums[:mid]),self.sortArray(nums[mid:])

        i=j=0
        il,jl=len(L),len(R)
        nums.clear()
        while i < il and j < jl:
            if L[i]<R[j]:
                nums.append(L[i])
                i+=1
            else:
                nums.append(R[j])
                j+=1
        if i<il:
            nums+=L[i:]
        else:
            nums+=R[j:]
        return nums

    def sortArray2(self, nums: List[int]) -> List[int]:
        # √ Accepted
        #     √ 10/10 cases passed (148 ms)
        #     √ Your runtime beats 99.49 % of python3 submissions
        #     √ Your memory usage beats 100 % of python3 submissions (19.2 MB)
        nums.sort()
        return nums
