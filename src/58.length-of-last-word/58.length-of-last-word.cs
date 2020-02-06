/*
 * @lc app=leetcode id=58 lang=csharp
 *
 * [58] Length of Last Word
 */
//  Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

// If the last word does not exist, return 0.

// Note: A word is defined as a character sequence consists of non-space characters only.

// Example:

// Input: "Hello World"
// Output: 5
public class Solution {
    public int LengthOfLastWord (string s) {
        // Accepted
        // 59/59 cases passed (76 ms)
        // Your runtime beats 100 % of csharp submissions
        // Your memory usage beats 71.7 % of csharp submissions (21.3 MB)        int r = s.Length - 1, res = 0;
        while (r > -1 && s[r] == ' ') --r;
        while (r > -1 && s[r] != ' ') {--r;++res; }
        return res;
    }
}