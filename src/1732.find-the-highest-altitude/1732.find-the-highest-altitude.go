/*
 * @lc app=leetcode.cn id=1732 lang=golang
 *
 * [1732] 找到最高海拔
 */

// @lc code=start
func largestAltitude(gain []int) int {
	// Accepted
	// 80/80 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 98.04 % of golang submissions (2 MB)
	res, cur := 0, 0
	for _, item := range gain {
		cur += item
		if cur > res {
			res = cur
		}
	}
	return res
}

// @lc code=end

