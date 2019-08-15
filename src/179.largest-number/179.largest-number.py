#
# @lc app=leetcode id=179 lang=python3
#
# [179] Largest Number
#
# √ Accepted
#   √ 222/222 cases passed (56 ms)
#   √ Your runtime beats 29.6 % of python3 submissions
#   √ Your memory usage beats 7.14 % of python3 submissions (13.9 MB)


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not nums or nums.count(0) == len(nums):
            return "0"
        lists = []
        numsl = len(nums)
        for i in range(numsl):
            nums_i_str = str(nums[i])
            if lists:
                inserted = False
                for j in range(len(lists)):
                    #if int(lists[j]+nums_i_str) < int(nums_i_str+lists[j]):
                    if lists[j]+nums_i_str < nums_i_str+lists[j]:
                        lists.insert(j, nums_i_str)
                        inserted = True
                        break
                if not inserted:
                    lists.append(nums_i_str)
            else:
                lists.append(nums_i_str)
        return "".join(lists)
