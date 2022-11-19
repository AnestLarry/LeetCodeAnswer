/*
 * @lc app=leetcode.cn id=1732 lang=rust
 *
 * [1732] 找到最高海拔
 */

// @lc code=start
impl Solution {
    pub fn largest_altitude(gain: Vec<i32>) -> i32 {
        // Accepted
        // 80/80 cases passed (4 ms) [WARN] Failed to get runtime percentile.
        let mut res = 0;
        let mut cur = 0;
        for item in gain {
            cur += item;
            if cur > res {
                res = cur;
            }
        }
        return res;
    }
}
// @lc code=end

