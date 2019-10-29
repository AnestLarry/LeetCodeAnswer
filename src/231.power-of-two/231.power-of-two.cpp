/*
 * @lc app=leetcode id=231 lang=cpp
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
Output: false*/
// @lc code=start
class Solution
{
public:
    bool isPowerOfTwo(int n)
    {
        // Accepted
        // 1108/1108 cases passed (0 ms)
        // Your runtime beats 100 % of cpp submissions
        // Your memory usage beats 72 % of cpp submissions (8.1 MB)
        return n > 0 && (n & (n - 1)) == 0;
    }
};
// @lc code=end
