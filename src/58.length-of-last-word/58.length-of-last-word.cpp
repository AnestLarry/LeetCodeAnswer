/*
 * @lc app=leetcode.cn id=58 lang=cpp
 *
 * [58] Length of Last Word
 */

// @lc code=start
class Solution
{
public:
    int lengthOfLastWord(string s)
    {
        int c = 0, i = s.size() - 1;
        while (i > 0 && s[i] == ' ')
        {
            i--;
        };
        while (i >= 0 && s[i--] != ' ')
        {
            c++;
        };
        return c;
    }
};
// @lc code=end
