#
# @lc app=leetcode id=75 lang=python3
#
# [75] Sort Colors
#
# √ Accepted
#   √ 87/87 cases passed (36 ms)
#   √ Your runtime beats 88.78 % of python3 submissions
#   √ Your memory usage beats 6.25 % of python3 submissions (13.7 MB)


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
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
