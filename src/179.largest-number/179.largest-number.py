#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# Given a list of non negative integers, arrange them such that they form the largest number.

# Example 1:

# Input: [10,2]
# Output: "210"
# Example 2:

# Input: [3,30,34,5,9]
# Output: "9534330"
# Note: The result may be very large, so you need to return a string instead of an integer.
import functools


class Solution:
    def largestNumber1(self, nums: List[int]) -> str:
        # Accepted
        # 222/222 cases passed (40 ms)
        # Your runtime beats 93.96 % of python3 submissions
        # Your memory usage beats 20 % of python3 submissions (13.7 MB)
        if not nums or nums.count(0) == len(nums):
            return "0"
        lists = []
        numsl = len(nums)
        for i in range(numsl):
            nums_i_str = str(nums[i])
            if lists:
                inserted = False
                for j in range(len(lists)):
                    if lists[j]+nums_i_str < nums_i_str+lists[j]:
                        lists.insert(j, nums_i_str)
                        inserted = True
                        break
                if not inserted:
                    lists.append(nums_i_str)
            else:
                lists.append(nums_i_str)
        return "".join(lists)

    def largestNumber(self, nums: List[int]) -> str:
        # Accepted
        # 222/222 cases passed (40 ms)
        # Your runtime beats 93.96 % of python3 submissions
        # Your memory usage beats 20 % of python3 submissions (13.7 MB)
        if not any(nums):
            return "0"
        return "".join(
            sorted(
                map(str, nums),
                key=functools.cmp_to_key(
                    lambda n1, n2: -1 if n1 + n2 > n2 +
                    n1 else (1 if n1+n2 < n2+n1 else 0)
                )
            )
        )
