/*
 * @lc app=leetcode id=344 lang=csharp
 *
 * [344] Reverse String
 */
// Write a function that reverses a string. The input string is given as an array of characters char[].

// Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

// You may assume all the characters consist of printable ascii characters.

// Example 1:

// Input: ["h","e","l","l","o"]
// Output: ["o","l","l","e","h"]
// Example 2:

// Input: ["H","a","n","n","a","h"]
// Output: ["h","a","n","n","a","H"]
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

