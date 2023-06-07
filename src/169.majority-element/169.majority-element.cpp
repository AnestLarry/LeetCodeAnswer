/*
 * @lc app=leetcode.cn id=169 lang=cpp
 *
 * [169] 多数元素
 */
#include <map>
#include <cmath>
// @lc code=start
class Solution
{
public:
    int majorityElement1(vector<int> &nums)
    {
        int len = nums.size();
        int s = std::ceil(len / 2);
        unordered_map<int, int> c = {};
        if (len < 2)
        {
            return nums[0];
        }
        for (int i = 0; i < len; i++)
        {
            if (c.count(nums[i]) == 1)
            {
                // c[nums[i]]++;
                if (++c[nums[i]] > s)
                {
                    return nums[i];
                }
            }
            else
            {
                c[nums[i]] = 1;
            }
        }
        return 0;
    }
    int majorityElement2(vector<int> &nums)
    {
        sort(nums.begin(), nums.end());
        return nums[nums.size() / 2];
    }
    int majorityElement(vector<int> &nums)
    {
        int c = 0, cur = nums[0];
        for (auto &&i : nums)
        {
            if (i == cur)
            {
                c++;
            }
            else
            {
                if (--c < 0)
                {
                    cur = i;
                    c = 1;
                }
            }
        }
        return cur;
    }
};
// @lc code=end
