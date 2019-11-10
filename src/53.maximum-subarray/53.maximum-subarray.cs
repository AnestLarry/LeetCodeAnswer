/*
 * @lc app=leetcode id=53 lang=csharp
 *
 * [53] Maximum Subarray
 */
/*Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle. */
// @lc code=start
public class Solution
{
    public int MaxSubArray(int[] nums)
    {
        // Accepted
        // 202/202 cases passed (96 ms)
        // Your runtime beats 84.72 % of csharp submissions
        // Your memory usage beats 10 % of csharp submissions (25 MB)
        int nums_len = nums.Length, maxnum = nums[0];
        if (nums_len == 1)
        {
            return nums[0];
        }
        int[] dp = new int[nums_len];
        dp[0] = nums[0];
        foreach (int i in Enumerable.Range(1, nums_len - 1))
        {
            if (dp[i - 1] > 0)
            {
                dp[i] = dp[i - 1] + nums[i];
            }
            else
            {
                dp[i] = nums[i];
            }
            if (dp[i] > maxnum)
            {
                maxnum = dp[i];
            }
        }
        return maxnum;
    }
}
// @lc code=end