#
# @lc app=leetcode id=412 lang=python3
#
# [412] Fizz Buzz
#
# Write a program that outputs the string representation of numbers from 1 to n.

# But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

# Example:

# n = 15,

# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]
class Solution:
    def fizzBuzz1(self, n: int) -> List[str]:
        # √ Accepted
        # √ 8/8 cases passed (268 ms)
        # √ Your runtime beats 6.04 % of python3 submissions
        # √ Your memory usage beats 5.33 % of python3 submissions (14.8 MB)
        result=[]
        while n>0:
            if n%5 == 0:
                if n%3==0:
                    result=["FizzBuzz"]+result
                    n-=1
                    continue
                result=["Buzz"]+result
                n-=1
            elif n%3 == 0:
                result=["Fizz"]+result
                n-=1
            else:
                result=[str(n)]+result
                n-=1
        return result

    def fizzBuzz(self, n: int) -> List[str]:
        # √ Accepted
        # √ 8/8 cases passed (36 ms)
        # √ Your runtime beats 100 % of python3 submissions
        # √ Your memory usage beats 5.33 % of python3 submissions (14.7 MB)
        result=[]
        for i in range(1,n+1):
            if i%5 == 0:
                if i%3 == 0:
                    result+=["FizzBuzz"]
                    continue
                result+=["Buzz"]
            elif i%3==0:
                result+=["Fizz"]
            else:
                result+=[str(i)]
        return result
