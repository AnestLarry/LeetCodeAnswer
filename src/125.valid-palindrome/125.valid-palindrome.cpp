/*
 * @lc app=leetcode.cn id=125 lang=cpp
 *
 * [125] Valid Palindrome
 */

// @lc code=start
class Solution
{
public:
    bool isPalindrome(string s)
    {
        int len = s.size();
        int left = 0, right = len - 1;
        while (left < right)
        {
            while (left < right && !checkvalid(s[left]))
                left++;
            while (left < right && !checkvalid(s[right]))
                right--;
            if (toUpper(s[left]) == toUpper(s[right]))
            {
                left++;
                right--;
            }
            else
            {
                return false;
            }
        }
        return true;
    }

    inline bool checkvalid(char c)
    {
        return (96 < c && c < 123) || (64 < c && c < 91) || (47 < c && c < 58);
    }

    inline char toUpper(char c)
    {
        return c > 90 ? c - 32 : c;
    }
};
// @lc code=end
