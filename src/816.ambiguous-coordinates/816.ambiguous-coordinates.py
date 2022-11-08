#
# @lc app=leetcode.cn id=816 lang=python3
#
# [816] 模糊坐标
# We had some 2-dimensional coordinates, like "(1, 3)" or "(2, 0.5)". Then, we removed all commas, decimal points, and spaces and ended up with the string s.

# For example, "(1, 3)" becomes s = "(13)" and "(2, 0.5)" becomes s = "(205)".
# Return a list of strings representing all possibilities for what our original coordinates could have been.

# Our original representation never had extraneous zeroes, so we never started with numbers like "00", "0.0", "0.00", "1.0", "001", "00.01", or any other number that can be represented with fewer digits. Also, a decimal point within a number never occurs without at least one digit occurring before it, so we never started with numbers like ".1".

# The final answer list can be returned in any order. All coordinates in the final answer have exactly one space between them (occurring after the comma.)

#  

# Example 1:

# Input: s = "(123)"
# Output: ["(1, 2.3)","(1, 23)","(1.2, 3)","(12, 3)"]
# Example 2:

# Input: s = "(0123)"
# Output: ["(0, 1.23)","(0, 12.3)","(0, 123)","(0.1, 2.3)","(0.1, 23)","(0.12, 3)"]
# Explanation: 0.0, 00, 0001 or 00.01 are not allowed.
# Example 3:

# Input: s = "(00011)"
# Output: ["(0, 0.011)","(0.001, 1)"]
#  

# Constraints:

# 4 <= s.length <= 12
# s[0] == '(' and s[s.length - 1] == ')'.
# The rest of s are digits.


# @lc code=start
class Solution:
    def ambiguousCoordinates(self, s: str) -> List[str]:
        # Accepted
        # 346/346 cases passed (44 ms)
        # Your runtime beats 73.53 % of python3 submissions
        # Your memory usage beats 37.25 % of python3 submissions (15.2 MB)
        s = s[1:-1]
        res: List[str] = []
        for i in range(1, len(s)):
            lt = self.get_pos(s[:i])
            if len(lt) == 0:
                continue
            rt = self.get_pos(s[i:])
            if len(rt) == 0:
                continue
            for i, j in product(lt, rt):
                res.append('(' + i + ', ' + j + ')')
        return res

    def get_pos(self, s: str) -> List[str]:
        pos: List[str] = []
        if s[0] != '0' or s == '0':
            pos.append(s)
        for p in range(1, len(s)):
            if p != 1 and s[0] == '0' or s[-1] == '0':
                continue
            pos.append(s[:p] + "." + s[p:])
        return pos
# @lc code=end
