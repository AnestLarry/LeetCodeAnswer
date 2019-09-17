#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        #√ Accepted
        #   √ 34/34 cases passed (36 ms)
        #   √ Your runtime beats 75.98 % of python3 submissions
        #   √ Your memory usage beats 7.69 % of python3 submissions (13.7 MB)
        pascal = [1]*(rowIndex + 1)
        for i in range(2,rowIndex+1):
            for j in range(i-1,0,-1):
                pascal[j] += pascal[j-1]
        return pascal
    # Error Code
    # def getRow2(self, rowIndex: int) -> List[int]:
    #     if rowIndex < 1:
    #         return []
    #     elif rowIndex ==1:
    #         return [[1]]
    #     result = [1]*(rowIndex+1)
    #     l,r = 1,rowIndex-2
    #     while l<=r:
    #         print(l,r)
    #         print(self.Permutation_Number_Formula(rowIndex,l))
    #         print(self.factorial(l))
    #         result[l] = result[r] = \
    #             self.Permutation_Number_Formula(rowIndex,l) / self.factorial(l)
    #         l += 1
    #         r -= 1
    #     return result

    # def Permutation_Number_Formula(self,n:int,m:int):
    #     s=1
    #     for i in range(n,n-m+1,-1):
    #         s*=i
    #     return s 
    
    # def factorial(self,n:int):
    #     s=1
    #     for i in range(n,2,-1):
    #         s*=i
    #     return s
