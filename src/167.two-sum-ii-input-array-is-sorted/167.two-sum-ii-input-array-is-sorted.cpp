/*
 * @lc app=leetcode.cn id=167 lang=cpp
 *
 * [167] Two Sum II - Input array is sorted
 */
#include <vector>
// @lc code=start
class Solution
{
public:
    vector<int> twoSum(vector<int> &numbers, int target)
    {
        std::vector<int> res(2);
        int len = numbers.size();
        int end = len - 1;
        while (end > 1 && numbers[end] > target-numbers[0])
        {
            end--;
        }
        for (int i = 0; i < end; i++)
        {
            int left = i+1, right = end;
            while (left <= right)
            {
                int mid = (left + right) >> 1;
                int temp = numbers[i] + numbers[mid];
                if (temp == target)
                {
                    res[0] = i + 1;
                    res[1] = mid + 1;
                    return res;
                }
                else if (temp < target)
                {
                    left = mid + 1;
                }
                else
                {
                    right = mid - 1;
                    end = right;
                }
            }
        }
        return res;
    }
};
// @lc code=end
