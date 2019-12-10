/*
 * @lc app=leetcode id=263 lang=golang
 *
 * [263] Ugly Number
 */
//  Write a program to check whether a given number is an ugly number.

//  Ugly numbers are positive numbers whose prime factors only include 2, 3, 5.

//  Example 1:

//  Input: 6
//  Output: true
//  Explanation: 6 = 2 × 3
//  Example 2:

//  Input: 8
//  Output: true
//  Explanation: 8 = 2 × 2 × 2
//  Example 3:

//  Input: 14
//  Output: false
//  Explanation: 14 is not ugly since it includes another prime factor 7.
//  Note:

//  1 is typically treated as an ugly number.
//  Input is within the 32-bit signed integer range: [−231,  231 − 1].
// @lc code=start
func isUgly(num int) bool {
	// Accepted
	// 1012 / 1012 test cases passed (0 ms)
	// Your runtime beats 100.00% of csharp submissions
	// Your memory usage beats 50.00% of csharp submissions (2.2 MB)
	if num < 1 {
		return false
	}
	for num%2 == 0 {
		num /= 2
	}
	for num%3 == 0 {
		num /= 3
	}
	for num%5 == 0 {
		num /= 5
	}
	if num == 1 {
		return true
	} else {
		return false
	}
}

// @lc code=end
