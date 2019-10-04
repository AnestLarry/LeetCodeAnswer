/*
 * @lc app=leetcode id=28 lang=csharp
 *
 * [28] Implement strStr()
 */
//  Implement strStr().

// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// Example 1:

// Input: haystack = "hello", needle = "ll"
// Output: 2
// Example 2:

// Input: haystack = "aaaaa", needle = "bba"
// Output: -1
// Clarification:

// What should we return when needle is an empty string? This is a great question to ask during an interview.

// For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
public class Solution
{
    public int StrStr(string haystack, string needle)
    {
        // √ Accepted
        //   √ 74/74 cases passed (80 ms)
        //   √ Your runtime beats 68.45 % of csharp submissions
        //   √ Your memory usage beats 6.67 % of csharp submissions (21.6 MB)
        if (needle == null)
        {
            return 0;
        }
        int nl = needle.Length;
        for (int i = 0; i < haystack.Length - nl + 1; i++)
        {
            if (haystack.Substring(i, nl) == needle)
            {
                return i;
            }
        }
        return -1;
    }
}
