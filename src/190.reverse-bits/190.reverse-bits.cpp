/*
 * @lc app=leetcode id=190 lang=cpp
 *
 * [190] Reverse Bits
 */
/*
Accepted
600/600 cases passed (0 ms)
Your runtime beats 100 % of cpp submissions
Your memory usage beats 38.27 % of cpp submissions (6.1 MB)
*/
// @lc code=start
class Solution {
public:
    uint32_t reverseBits(uint32_t n) {
        uint32_t m=0,res =0;
        for(;res<32;res++){
            m = m<<1 | n>>res&1;
        }
        return m;
    }
};
// @lc code=end

