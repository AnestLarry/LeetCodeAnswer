/*
 * @lc app=leetcode.cn id=27 lang=cpp
 *
 * [27] 移除元素
 */

// @lc code=start
class Solution
{
public:
    int removeElement1(vector<int> &nums, int val)
    {
        int i = 0, j = nums.size() - 1, temp;
        while (i <= j)
        {
            if (nums[i] == val)
            {
                temp = nums[i];
                nums[i] = nums[j];
                nums[j] = temp;
                j -= 1;
            }
            else
            {
                i++;
            }
        }
    }
    int removeElement2(vector<int> &nums, int val)
    {
        int i = 0, j = nums.size();
        if (j == 0)
        {
            return 0;
        }
        while (i < j && nums[i] != val)
        {
            i++;
        }
        j--;
        while (i < j)
        {
            while (i <= j && nums[j] == val)
            {
                j--;
            }
            while (i <= j && nums[i] != val)
            {
                i++;
            }
            if (i > j)
            {
                break;
            }
            int temp = nums[i];
            nums[i] = nums[j];
            nums[j] = temp;
            i++;
        }
        return i;
    }
};
// @lc code=end
