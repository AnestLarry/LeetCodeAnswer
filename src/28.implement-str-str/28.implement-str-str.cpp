/*
 * @lc app=leetcode.cn id=28 lang=cpp
 *
 * [28] Implement strStr()
 */
#include <string>
// @lc code=start
class Solution
{
public:
    int strStr(std::string haystack, std::string needle)
    {
        int hlen = haystack.size(), nlen = needle.size();
        if (nlen == 0)
            return 0;
        int next[nlen];
        std::fill(next, next + nlen, 0);
        for (int i = 1, j = 0; i < nlen; i++)
        {
            while (j > 0 && needle[i] != needle[j])
            {
                j = next[j - 1];
            }
            if (needle[i] == needle[j])
            {
                j++;
            }
            next[i] = j;
        }
        for (int i = 0, j = 0; i <= hlen; i++)
        {
            while (j > 0 && haystack[i] != needle[j])
                j = next[j-1];
            if (haystack[i] == needle[j])
                j++;
            if (j == nlen)
                return i-nlen+1;
        }
        return -1;
    }
};
// @lc code=end
