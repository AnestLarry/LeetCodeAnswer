/*
 * @lc app=leetcode id=14 lang=csharp
 *
 * [14] Longest Common Prefix
 */
//  Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
// Note:

// All given inputs are in lowercase letters a-z.
public class Solution
{
    public string LongestCommonPrefix(string[] strs)
    {
        // Accepted
        // 118/118 cases passed (116 ms)
        // Your runtime beats 91.41 % of csharp submissions
        // Your memory usage beats 11.29 % of csharp submissions (23.7 MB)
        string res = "";
        if (strs == null || strs.Length == 0 || strs.Length == 1)
        {
            return strs.Length == 1 ? strs[0] : res;
        }
        for (int i = 0; i < strs[0].Length; i++)
        {
            try
            {
                foreach (string s in strs)
                {
                    if (strs[0][i] != s[i])
                    {
                        return res;
                    }
                }
                res += strs[0][i];
            }
            catch
            {
                return res;
            }
        }
        return res;
    }
}
