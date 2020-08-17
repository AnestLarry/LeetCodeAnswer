/*
 * @lc app=leetcode id=190 lang=csharp
 *
 * [190] Reverse Bits
 */
/*
Accepted
600/600 cases passed (48 ms)
Your runtime beats 82.47 % of csharp submissions
Your memory usage beats 66.67 % of csharp submissions (15 MB)
*/
// @lc code=start
public class Solution {
        public uint reverseBits(uint n) {
        uint m=0;
        for(int res=0;res<32;res++){
            m=m<<1|n>>res&1;
        }
        return m;
    }
}
// @lc code=end

