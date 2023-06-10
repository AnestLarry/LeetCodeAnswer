/*
 * @lc app=leetcode.cn id=45 lang=cpp
 *
 * [45] Jump Game II
 */

// @lc code=start
class Solution
{
public:
    int jump(vector<int> &nums)
    {
        int j = 0;
        int end = 0;
        int t = 0;
        int len = nums.size();
        for (int i = 0; i < len - 1; i++)
        {
            t = t > nums[i] + i ? t : nums[i] + i;
            if (i == end)
            {
                end = t;
                j++;
            }
        }
        return j;
    }
};
// @lc code=end
