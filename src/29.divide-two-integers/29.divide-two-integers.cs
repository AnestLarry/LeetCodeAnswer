/*
 * @lc app=leetcode.cn id=29 lang=csharp
 *
 * [29] Divide Two Integers
 */
// Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

// Return the quotient after dividing dividend by divisor.

// The integer division should truncate toward zero.

// Example 1:

// Input: dividend = 10, divisor = 3
// Output: 3
// Example 2:

// Input: dividend = 7, divisor = -3
// Output: -2
// Note:
// Both dividend and divisor will be 32-bit signed integers.
// The divisor will never be 0.

// Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

// @lc code=start
public class Solution
{
    public int Divide(int dividend, int divisor)
    {
        // Top Voted
        // Accepted
        // 989/989 cases passed (48 ms)
        // Your runtime beats 76.6 % of csharp submissions
        // Your memory usage beats 8.33 % of csharp submissions (14.5 MB)
        if (divisor == 0 || (dividend == Int32.MinValue && divisor == -1)) return Int32.MaxValue;
        bool flag = dividend > 0 ^ divisor > 0;
        if (dividend > 0) dividend = 0 - dividend;
        if (divisor > 0) divisor = 0 - divisor;
        int[] nums = new int[32], counts = new int[32];
        nums[0] = divisor;
        counts[0] = -1;
        int i = 1;
        int temp = nums[0] << 1;
        while (temp < 0 && temp >= dividend)
        {
            nums[i] = temp;
            counts[i] = counts[i - 1] << 1;
            temp = nums[i++] << 1;
        }
        int result = 0;
        while (--i >= 0)
        {
            if (dividend <= nums[i])
            {
                result += counts[i];
                dividend -= nums[i];
            }
        }
        return flag ? result : 0 - result;
    }
    public int Divide2(int dividend, int divisor)
    {
        // Accepted
        // 989/989 cases passed (44 ms)
        // Your runtime beats 97.87 % of csharp submissions
        // Your memory usage beats 8.33 % of csharp submissions (14.2 MB)
        long res = 0, dividend_ = dividend, divisor_ = divisor;
        res = dividend / divisor;
        if (res >= ~(1 << 31))
            return ~(1 << 31);
        else if (res <= (1 << 31))
            return 1 << 31;
        else
            return (int)res;
    }
}
// @lc code=end

