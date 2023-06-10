/*
 * @lc app=leetcode.cn id=238 lang=cpp
 *
 * [238] Product of Array Except Self
 */
#include <vector>
// @lc code=start
class Solution
{
public:
    vector<int> productExceptSelf(std::vector<int> &nums)
    {
        int n = nums.size();
        int left = 1, right = 1; // left：从左边累乘，right：从右边累乘
        std::vector<int> res(n, 1);
        for (int i = 0; i < n; ++i) // 最终每个元素其左右乘积进行相乘得出结果
        {
            res[i] *= left; // 乘以其左边的乘积
            left *= nums[i];
            res[n - 1 - i] *= right; // 乘以其右边的乘积
            right *= nums[n - 1 - i];
        }
        return res;
    }
    vector<int> productExceptSelf2(std::vector<int> &nums)
    {
        int zs = 0;
        int zi = -1;
        int len = nums.size();
        long long r = 1;
        for (int i = 0; i < len; i++)
        {
            if (nums[i] == 0)
            {
                zs++;
                zi = i;
            }
            else
            {
                r *= nums[i];
            }
        }
        std::vector<int> res(len, 0);
        if (zs > 1)
        {
            return res;
        }
        else if (zs == 1)
        {
            res[zi] = r;
            return res;
        }
        for (int i = 0; i < len; i++)
        {
            res[i] = r / nums[i];
        }
        return res;
    }
};
// @lc code=end
