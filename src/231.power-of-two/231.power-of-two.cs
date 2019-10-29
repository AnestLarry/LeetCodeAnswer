/*
 * @lc app=leetcode id=231 lang=csharp
 *
 * [231] Power of Two
 */
/*Given an integer, write a function to determine if it is a power of two.

Example 1:

Input: 1
Output: true 
Explanation: 20 = 1
Example 2:

Input: 16
Output: true
Explanation: 24 = 16
Example 3:

Input: 218
Output: false */
// @lc code=start
public class Solution
{
    public bool IsPowerOfTwo(int n)
    {
        // Accepted
        // 1108/1108 cases passed (32 ms)
        // Your runtime beats 100 % of csharp submissions
        // Your memory usage beats 10 % of csharp submissions (14.2 MB)
        return (n > 0) && (n & (n - 1)) == 0;
    }
}
// @lc code=end

