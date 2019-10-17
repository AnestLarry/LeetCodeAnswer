/*
 * @lc app=leetcode id=344 lang=csharp
 *
 * [344] Reverse String
 */

// @lc code=start
public class Solution
{
    public void ReverseString(char[] s)
    {
        // Accepted
        // 478/478 cases passed (396 ms)
        // Your runtime beats 63.16 % of csharp submissions
        // Your memory usage beats 11.54 % of csharp submissions (33.7 MB)
        char temp;
        int l = 0, r = s.Length-1;
        for (; l < r; l++, r--)
        {

            temp = s[l];
            s[l] = s[r];
            s[r] = temp;
        }
    }
}
// @lc code=end

