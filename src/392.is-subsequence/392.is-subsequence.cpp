/*
 * @lc app=leetcode.cn id=392 lang=cpp
 *
 * [392] Is Subsequence
 */

// @lc code=start
class Solution
{
public:
     bool isSubsequence(string s, string t)
    {
        int tlen = t.size(), slen = s.size();
        if(slen == 0)return true;
        if(tlen == 0 )return false;
        for (int i = 0, j = 0; i <slen ; i++)
        {
            while (j < tlen && s[i] != t[j])
            {
                j++;
            }
            if (j>=tlen && s[slen-1] != t[j-1])
            {
                return false;
            }
            j++;
        }
        return true;
    }
};
// @lc code=end
