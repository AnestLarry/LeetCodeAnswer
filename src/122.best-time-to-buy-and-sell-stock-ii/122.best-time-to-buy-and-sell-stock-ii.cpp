/*
 * @lc app=leetcode.cn id=122 lang=cpp
 *
 * [122] Best Time to Buy and Sell Stock II
 */

// @lc code=start
class Solution {
public:
    int maxProfit(vector<int>& prices)    {
        int r = 0;
        int s = 0;
        int len = prices.size();
        for (int i = 1; i < len; i++)
        {
            if (prices[i] - prices[i - 1] > 0)
            {
                s = i - 1;
                i++;
                while (i < len && (prices[i] - prices[s] >= prices[i - 1] - prices[s]))
                {
                    i++;
                }
                r += prices[i - 1] - prices[s];
            }
        }
        return r;
    }
};
// @lc code=end
