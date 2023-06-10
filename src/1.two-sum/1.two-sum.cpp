/*
 * @lc app=leetcode.cn id=1 lang=cpp
 *
 * [1] two-sum
 */
#include <unordered_map>
#include<vector>
// @lc code=start
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        std::unordered_map<int,int> cache;
        std::vector<int> res{-1,-1};
        int len = nums.size();
        for (int i = 0; i < len; i++)
        {
            if (cache.count(target - nums[i])==1)
            {
                res[0] = cache[target - nums[i]];
                res[1] = i;
                return res;
            }else{
                cache[nums[i]] = i;
            }
            
        }
        return res;
    }
};
// @lc code=end

