#
# @lc app=leetcode id=415 lang=python3
#
# [415] Add Strings
#
# Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

# Note:

# The length of both num1 and num2 is < 5100.
# Both num1 and num2 contains only digits 0-9.
# Both num1 and num2 does not contain any leading zero.
# You must not use any built-in BigInteger library or convert the inputs to integer directly.
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        # √ Accepted
        #   √ 315/315 cases passed (44 ms)
        #   √ Your runtime beats 83.43 % of python3 submissions
        #   √ Your memory usage beats 5.55 % of python3 submissions (14.3 MB)
        b, s, bl, sl = 0, 0, 0, 0
        l1, l2 = len(num1), len(num2)
        if l1 > l2:
            b, s, bl, sl = num1, num2, l1, l2
        else:
            b, s, bl, sl = num2, num1, l2, l1
        flag, result = False, []
        for i in zip([b[i] for i in range(bl-1, -1, -1)], [s[i] for i in range(sl-1, -1, -1)]):
            if flag:
                Sum = int(i[0])+int(i[1])+1
                flag = False
            else:
                Sum = int(i[0])+int(i[1])
            if Sum > 9:
                result.append(str(Sum % 10))
                flag = True
            else:
                result.append(str(Sum))
        i = bl - sl - 1
        while i > -1:
            if flag:
                Sum = int(b[i])+1
                flag = False
                if Sum > 9:
                    result.append(str(Sum % 10))
                    flag = True
                else:
                    result.append(str(Sum))
            else:
                result.append(b[i])
            i -= 1
        if flag:
            result.append("1")
        return "".join([result[i] for i in range(len(result)-1, -1, -1)])
