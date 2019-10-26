/*
 * @lc app=leetcode id=190 lang=csharp
 *
 * [190] Reverse Bits
 */

// @lc code=start
public class Solution {
        public uint reverseBits2(uint n) {
        // Accepted
        // 600/600 cases passed (40 ms)
        // Your runtime beats 95.42 % of csharp submissions
        // Your memory usage beats 20 % of csharp submissions (14.2 MB)
        uint m=0;
        int res=0;
        while(res<32){
            m=m<<1|n>>res&1;
            res+=1;
        }
        return m;
    }
}
// @lc code=end

