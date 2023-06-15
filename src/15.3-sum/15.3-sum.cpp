/*
 * @lc app=leetcode.cn id=15 lang=cpp
 *
 * [15] 3Sum
 */
#include <vector>
#include <algorithm>
// @lc code=start
class Solution
{
public:
    std::vector<std::vector<int>> threeSum(std::vector<int> &nums)
    {
        std::vector<std::vector<int>> res;
        std::vector<int> r;
        std::sort(nums.begin(), nums.end());
        int len = nums.size();
        for (vector<int>::iterator i = nums.begin(); i <= nums.end() - 3; i++) // 最起码三个数
        {
            if (*i > 0)
                break;
            if (distance(nums.begin(), i) > 0 && *i == *(i - 1)) // 重复的数不重复// 问题在这里 i=0解引用出错
            {
                continue;
            }
            vector<int>::iterator left = i + 1, right = nums.end() - 1;
            while (left < right)
            {
                int temp = *i + *left + *right;
                if (temp == 0)
                {
                    r.clear();
                    r.push_back(*i);
                    r.push_back(*left);
                    r.push_back(*right);
                    res.push_back(r);
                    left++;
                    right--;
                    while(*right==*(right+1) && left<right)
                    {
                        right--;
                    }
                    while(*left==*(left-1) && left<right)
                    {
                        left++;
                    }
                }
                else if (temp < 0)
                {
                    left++;
                }
                else
                {
                    right--;
                }
            }
        }
        return res;
    }
};
// @lc code=end
