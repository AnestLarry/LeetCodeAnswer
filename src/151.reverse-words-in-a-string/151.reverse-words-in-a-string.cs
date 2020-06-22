/*
 * @lc app=leetcode id=151 lang=csharp
 *
 * [151] Reverse Words in a String
 */
 /*
 Given an input string, reverse the string word by word.


Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
 */
using System;
using System.Text.RegularExpressions;
public class Solution {
    public string ReverseWords (string s) {
        // Accepted
        // 25/25 cases passed (92 ms)
        // Your runtime beats 99.29 % of csharp submissions
        // Your memory usage beats 100 % of csharp submissions (24.7 MB)
        string[] sl = s.Split ();
        Array.Reverse (sl);
        return String.Join (" ", from x in sl where x.Length > 0 select x.Trim (' '));
    }

    public string ReverseWords2 (string s) {
        // Accepted
        // 25/25 cases passed (120 ms)
        // Your runtime beats 47.82 % of csharp submissions
        // Your memory usage beats 100 % of csharp submissions (27.5 MB)
        string pattern = @"[^ ]+";
        List<string> result = new List<string> { };
        foreach (Match m in Regex.Matches (s, pattern)) {
            result.Insert (0, m.Value);
        }
        return string.Join (" ", result);
    }
}