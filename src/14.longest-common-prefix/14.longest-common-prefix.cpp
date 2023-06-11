/*
 * @lc app=leetcode.cn id=14 lang=cpp
 *
 * [14] Longest Common Prefix
 */
#include<string>
#include<vector>
// @lc code=start
class Solution {
public:
    string longestCommonPrefix(std::vector<std::string>& strs) {
        int len = strs.size();
        if (len < 2)
        {
            return len == 1 ? strs[0] : "";
        }
        int c = 0;
        for (int i = 0; i < strs[0].size(); i++)
        {
            bool flag = true;
            for (int j = 0; j < len; j++)
            {
                if (strs[j][i] != strs[0][i])
                {
                    flag = false;
                    break;
                }
            }
            if (flag)   
            {
                c++;
            }else{
                break;
            }
        }
        return strs[0].substr(0,c);
    }
};
// @lc code=end

