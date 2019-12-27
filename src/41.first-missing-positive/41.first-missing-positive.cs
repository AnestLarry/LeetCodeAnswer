/*
 * @lc app=leetcode.cn id=41 lang=csharp
 *
 * [41] First Missing Positive
 */
/*Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.*/
// @lc code=start
public class Solution
{
    public int FirstMissingPositive(int[] nums)
    {
        // Accepted
        // 165/165 cases passed (104 ms)
        // Your runtime beats 90.91 % of csharp submissions
        // Your memory usage beats 5.26 % of csharp submissions (23.6 MB)
        if (nums == null)
        {
            return 1;
        }
        for (int i = 1; i < nums.Length + 2; i++)
        {
            if (Array.IndexOf(nums, i) < 0)
            {
                return i;
            }
        }
        return 1;
    }
}
// @lc code=end

