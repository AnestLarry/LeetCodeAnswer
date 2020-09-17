/*
 * @lc app=leetcode.cn id=202 lang=csharp
 *
 * [202] Happy Number
 */
// Write an algorithm to determine if a number is "happy".

// A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

// Example:

// Input: 19
// Output: true
// Explanation:
// 12 + 92 = 82
// 82 + 22 = 68
// 62 + 82 = 100
// 12 + 02 + 02 = 1
// @lc code=start
public class Solution {
    public bool IsHappy (int n) {
        // Accepted
        // 401/401 cases passed (48 ms)
        // Your runtime beats 82.55 % of csharp submissions
        // Your memory usage beats 40.23 % of csharp submissions (16.7 MB)
        HashSet<int> repeat = new HashSet<int> () { n };
        while (n != 1) {
            int nn = 0;
            while (n > 0) {
                int d = n % 10;
                nn += d * d;
                n = n / 10;
            }
            if (!repeat.Add (nn))
                return false;
            n = nn;
        }
        return true;
    }
}
// @lc code=end