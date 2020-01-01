/*
 * @lc app=leetcode id=53 lang=c
 *
 * [53] Maximum Subarray
 */
/*Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.*/
// @lc code=start

int maxSubArray(int *nums, int numsSize)
{
    // Accepted
    // 202/202 cases passed (8 ms)
    // Your runtime beats 88.41 % of c submissions
    // Your memory usage beats 82.17 % of c submissions (7.6 MB)
    if (numsSize == 1)
    {
        return nums[0];
    }
    int bl = nums[0], maxnum = nums[0], i;
    for (i = 1; i < numsSize; i++)
    {
        bl = bl > 0 ? bl + nums[i] : nums[i];
        if (bl > maxnum)
        {
            maxnum = bl;
        }
    }
    return maxnum;
}

// @lc code=end