#
# @lc app=leetcode.cn id=1704 lang=python3
#
# [1704] 判断字符串的两半是否相似
#

# @lc code=start
class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        # Accepted
        # 113/113 cases passed (28 ms)
        # Your runtime beats 100.00 % of python3 submissions
        # Your memory usage beats 85.31 % of python3 submissions (15 MB)
        return len([x for x in s[:len(s) >> 1] if x.lower() in "aeiou"]) \
            == \
            len([x for x in s[len(s) >> 1:] if x.lower() in "aeiou"])
# @lc code=end
