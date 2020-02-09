/*
 * @lc app=leetcode.cn id=69 lang=csharp
 *
 * [69] Sqrt(x)
 */
// Implement int sqrt(int x).

// Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

// Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

// Example 1:

// Input: 4
// Output: 2
// Example 2:

// Input: 8
// Output: 2
// Explanation: The square root of 8 is 2.82842..., and since
// the decimal part is truncated, 2 is returned.
// @lc code=start
public class Solution {
    public int MySqrt (int x) {
        // Accepted
        // 1017/1017 cases passed (44 ms)
        // Your runtime beats 93.37 % of csharp submissions
        // Your memory usage beats 16.24 % of csharp submissions (14.1 MB)
        if (x == 0 || x == 1) {
            return x;
        }
        double guess = x * (2.0 / x);
        int temp = 0;
        while (true) {
            guess = (guess + x / guess) / 2;
            int t = (int) (guess);
            if (temp == t) {
                break;
            } else {
                temp = t;
            }
        }
        return temp;
    }
}
// @lc code=end