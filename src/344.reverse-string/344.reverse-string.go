/*
 * @lc app=leetcode id=344 lang=golang
 *
 * [344] Reverse String
 */

// @lc code=start
func reverseString(s []byte) {
	// Accepted
	// 478/478 cases passed (656 ms)
	// Your runtime beats 60.95 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (8.4 MB)
	l, r := 0, len(s)-1
	for l < r {
		s[l], s[r] = s[r], s[l]
		l, r = l+1, r-1
	}
}

// @lc code=end
