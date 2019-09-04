#
# @lc app=leetcode id=139 lang=python3
#
# [139] Word Break
#
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # √ Accepted
        #   √ 36/36 cases passed (40 ms)
        #   √ Your runtime beats 90.92 % of python3 submissions
        #   √ Your memory usage beats 5.55 % of python3 submissions (13.9 MB)
        l = len(s)
        if not wordDict: return not s
        bl = [False] * (l + 1)
        bl[0] = True
        for i in range(1, l + 1):
            for j in range(i - 1, -1, -1):
                if bl[j] and s[j:i] in wordDict:
                    bl[i] = True
                    break
        return bl[-1]
