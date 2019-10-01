/*
 * @lc app=leetcode id=151 lang=csharp
 *
 * [151] Reverse Words in a String
 */
using System.Text.RegularExpressions;
public class Solution
{
    public string ReverseWords(string s)
    {
        // √ Accepted
        //   √ 25/25 cases passed (108 ms)
        //   √ Your runtime beats 35.86 % of csharp submissions
        //   √ Your memory usage beats 14.29 % of csharp submissions (26.6 MB)
        string pattern = @"[^ ]+";
        List<string> result = new List<string> { };
        foreach (Match m in Regex.Matches(s, pattern))
        {
            result.Insert(0, m.Value);
        }
        return string.Join(" ", result);
    }
}
