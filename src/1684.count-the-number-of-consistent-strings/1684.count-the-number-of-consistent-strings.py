#
# @lc app=leetcode.cn id=1684 lang=python3
#
# [1684] 统计一致字符串的数目
#

# @lc code=start
class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        # Accepted
        # 74/74 cases passed (132 ms)
        # Your runtime beats 22.1 % of python3 submissions
        # Your memory usage beats 75.97 % of python3 submissions (16.6 MB)
        c: int = 0
        for w in words:
            for j in allowed:
                w = w.replace(j, "")
            if w == "":
                c += 1
        return c

    def countConsistentStrings2(self, allowed: str, words: List[str]) -> int:
        # Accepted
        # 74/74 cases passed (104 ms)
        # Your runtime beats 53.04 % of python3 submissions
        # Your memory usage beats 49.72 % of python3 submissions (16.6 MB)
        return sum(all(c in allowed for c in w) for w in words)
    
# @lc code=end
#r=re.compile("["+"|".join(list(allowed))+"]")