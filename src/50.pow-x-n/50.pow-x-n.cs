/*
 * @lc app=leetcode id=50 lang=csharp
 *
 * [50] Pow(x, n)
 Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
 */
public class Solution
{
    public double MyPow(double x, int n)
    {
        // Accepted
        // 304/304 cases passed (52 ms)
        // Your runtime beats 81.19 % of csharp submissions
        // Your memory usage beats 8 % of csharp submissions (14.7 MB)
        return Math.Pow(x, n);
    }
    public double MyPow2(double x, int n)
    {
        // Accepted
        // 304/304 cases passed (44 ms)
        // Your runtime beats 99.01 % of csharp submissions
        // Your memory usage beats 8 % of csharp submissions (14.6 MB)
        bool m = n<0;
        double p = 1;
        for (; n != 0; n /= 2)
        {
            if ((n & 1) == 1) p *= x;
            x *= x;
        }
        return m ? 1 / p : p;
    }
}
