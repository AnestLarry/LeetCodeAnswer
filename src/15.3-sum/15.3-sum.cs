/*
 * @lc app=leetcode.cn id=15 lang=csharp
 *
 * [15] 3Sum
 */
/*# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]*/
// @lc code=start
public class Solution
{
    public IList<IList<int>> ThreeSum(int[] nums)
    {
        // Accepted
        // 313/313 cases passed (368 ms)
        // Your runtime beats 93.53 % of csharp submissions
        // Your memory usage beats 11.11 % of csharp submissions (34.8 MB)
        List<IList<int>> res = new List<IList<int>>();
        int l = nums.Length;
        if (l <= 2)
        {
            return res;
        }
        Array.Sort(nums);

        for (int i = 0; i < l; i++)
        {
            if (i != 0 && nums[i] == nums[i - 1]) continue;
            int last = l - 1;
            int j = i + 1;
            while (j < last)
            {
                int s = nums[i] + nums[j] + nums[last];
                if (s == 0)
                {

                    res.Add(new List<int>() { nums[i], nums[j], nums[last] });
                    j += 1;
                    last -= 1;
                    while (j != (i + 1) && nums[j] == nums[j - 1] && j < last) j += 1;
                    while (last != (l - 1) && nums[last] == nums[last + 1] && last > j) last -= 1;
                }
                else
                {
                    if (s < 0)
                    {
                        j += 1;
                    }
                    else
                    {
                        last -= 1;
                    }
                }
            }
        }
        return res;
    }
}
// @lc code=end

