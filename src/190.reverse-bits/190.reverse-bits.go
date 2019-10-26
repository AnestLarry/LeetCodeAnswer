/*
 * @lc app=leetcode id=190 lang=golang
 *
 * [190] Reverse Bits
 */

// @lc code=start
func reverseBits(num uint32) uint32 {
	// Accepted
	// 600/600 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 25 % of golang submissions (2.4 MB)
	var m, res uint32 = 0, 0
	for res < 32 {
		m = m<<1 | num>>res&1
		res += 1
	}
	return m
}

// @lc code=end
