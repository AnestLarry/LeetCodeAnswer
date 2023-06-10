/*
 * @lc app=leetcode.cn id=274 lang=cpp
 *
 * [274] H-Index
 */

// @lc code=start
class Solution {
public:
    int hIndex(vector<int>& citations) {
        int h=0,i=citations.size()-1;
        std::sort(citations.begin(),citations.end());
        while (i>=0 && citations[i]>h)
        {
            h++;
            i--;
        }
        return h;
    }
};
// @lc code=end

