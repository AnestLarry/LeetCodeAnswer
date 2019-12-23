/*
 * @lc app=leetcode.cn id=29 lang=golang
 *
 * [29] Divide Two Integers
 */
//  Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

//  Return the quotient after dividing dividend by divisor.

//  The integer division should truncate toward zero.

//  Example 1:

//  Input: dividend = 10, divisor = 3
//  Output: 3
//  Example 2:

//  Input: dividend = 7, divisor = -3
//  Output: -2
//  Note:
//  Both dividend and divisor will be 32-bit signed integers.
//  The divisor will never be 0.

//  Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 231 − 1 when the division result overflows.

// @lc code=start
// func divide1(dividend int, divisor int) int {

// }
func divide(dividend int, divisor int) int {
	// Accepted
	// 989/989 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 44 % of golang submissions (2.5 MB)
	//var res, dividend_, divisor_ int64 = 0, int64(dividend), int64(divisor)
	var res int64 = 0
	res = int64(dividend / divisor)
	if res > (1<<31)-1 {
		return (1 << 31) - 1
	} else if res < (-1 << 31) {
		return -1 << 31
	} else {
		return int(res)
	}
}

// @lc code=end
