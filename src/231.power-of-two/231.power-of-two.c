/*
 * @lc app=leetcode id=231 lang=c
 *
 * [231] Power of Two
 */

// @lc code=start
// Given an integer, write a function to determine if it is a power of two.

// Example 1:

// Input: 1
// Output: true
// Explanation: 20 = 1
// Example 2:

// Input: 16
// Output: true
// Explanation: 24 = 16
// Example 3:

// Input: 218
// Output: false
bool isPowerOfTwo(int n)
{
    // Accepted
    // 1108/1108 cases passed (4 ms)
    // Your runtime beats 57.88 % of c submissions
    // Your memory usage beats 100 % of c submissions (6.6 MB)
    return n > 0 && (n & (n - 1)) == 0;
}

// @lc code=end
