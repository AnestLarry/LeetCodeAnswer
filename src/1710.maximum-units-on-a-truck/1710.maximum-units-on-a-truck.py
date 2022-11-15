#
# @lc app=leetcode.cn id=1710 lang=python3
#
# [1710] Maximum Units on a Truck
#
# You are assigned to put some amount of boxes onto one truck. You are given a 2D array boxTypes, where boxTypes[i] = [numberOfBoxesi, numberOfUnitsPerBoxi]:

# numberOfBoxesi is the number of boxes of type i.
# numberOfUnitsPerBoxi is the number of units in each box of the type i.
# You are also given an integer truckSize, which is the maximum number of boxes that can be put on the truck. You can choose any boxes to put on the truck as long as the number of boxes does not exceed truckSize.

# Return the maximum total number of units that can be put on the truck.

# @lc code=start
class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Accepted
        # 76/76 cases passed (40 ms)
        # Your runtime beats 96.88 % of python3 submissions
        # Your memory usage beats 82.15 % of python3 submissions (15.2 MB)
        boxTypes.sort(key=lambda x: x[1])
        res = 0
        i = len(boxTypes)-1
        while i > -1:
            box = boxTypes[i]
            if box[0] > truckSize:
                return res+truckSize*box[1]
            else:
                res += box[0] * box[1]
                truckSize -= box[0]
                i -= 1
        return res
# @lc code=end
