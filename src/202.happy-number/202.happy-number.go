/*
 * @lc app=leetcode.cn id=202 lang=golang
 *
 * [202] Happy Number
 */
// Write an algorithm to determine if a number is "happy".

// A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

// Example:

// Input: 19
// Output: true
// Explanation:
// 12 + 92 = 82
// 82 + 22 = 68
// 62 + 82 = 100
// 12 + 02 + 02 = 1
// @lc code=start
func isHappy(n int) bool {
	// Accepted
	// 401/401 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 5.06 % of golang submissions (2.2 MB)
	repeat := make(map[int]int)
	repeat[n] = 1
	for n != 1 {
		nn := 0
		for n > 0 {
			d := n % 10
			nn += d * d
			n = n / 10
		}
		_, b := repeat[nn]
		if b {
			return false
		} else {
			repeat[nn] = 1
		}
		n = nn
	}
	return true
}

// @lc code=end
