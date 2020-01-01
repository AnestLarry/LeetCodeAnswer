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
        // 202/202 cases passed (100 ms)
        // Your runtime beats 99.68 % of csharp submissions
        // Your memory usage beats 5.88 % of csharp submissions (24.3 MB)
        int maxnum = nums[0],dp = nums[0];
        if (nums.Length == 1)
        {
            return nums[0];
        }
        for (int i = 1; i < nums.Length; i++)
        {
            dp = dp > 0 ? dp + nums[i] : nums[i];
            maxnum = dp > maxnum?dp:maxnum;
        }
        return maxnum;
    }
}
// @lc code=end