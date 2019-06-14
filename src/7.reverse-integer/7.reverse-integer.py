#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#
# √ Accepted
#   √ 1032/1032 cases passed (36 ms)
#   √ Your runtime beats 89.74 % of python3 submissions
#   √ Your memory usage beats 25.96 % of python3 submissions (13.3 MB)
class Solution:
    def reverse(self, x: int) -> int:
        ## Solution 1:
        # smollerzero=False
        # s,res=str(x),""
        # if s[0]=="-":
        #     smollerzero =True
        #     s=s[1:]
        # l=len(s)-1
        # while l>-1:
        #     res+=s[l]
        #     l-=1
        # if smollerzero:
        #     res = int(res)*-1
        # else:
        #     res=int(res)
        # if res > 2147483647 or res <= -2147483648:
        #     return 0
        # else:
        #     return res
        smollerzero=False
        s,p,seq,res = str(x),0,0,0
        l = len(s)
        while p<l:
            if s[p] == "-":
                p+=1
                smollerzero=True
                continue
            res+=int(s[p])*10**seq
            p,seq = p+1,seq+1
        if smollerzero:
            res*=-1
        if res > 2147483647 or res <= -2147483648:
            return 0
        else:
            return res

