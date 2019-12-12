/*
 * @lc app=leetcode.cn id=7 lang=golang
 *
 * [7] Reverse Integer
 */
/*Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.*/

// @lc code=start
func reverse(x int) int {
	// Accepted
	// 1032/1032 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 92.24 % of golang submissions (2.2 MB)
	var res int64 = 0
	for x != 0 {
		res = res*10 + int64(x%10)
		if res > 1<<31-1 || res < -1<<31 {
			return 0
		}
		x /= 10
	}
	return int(res)
}

// @lc code=end
