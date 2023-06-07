/*
 * @lc app=leetcode.cn id=26 lang=cpp
 *
 * [26] 删除有序数组中的重复项
 */

// @lc code=start
class Solution
{
public:
    int removeDuplicates(vector<int> &nums)
    {
        int cur = 0;
        int len = nums.size();
        for (int i = 1; i < len; i++)
        {
            if (nums[cur] < nums[i])
            {
                nums[++cur] = nums[i];

            }
        }
        return cur+1;
    }
};
// @lc code=end
