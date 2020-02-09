/*
 * @lc app=leetcode.cn id=69 lang=golang
 *
 * [69] Sqrt(x)
 */
// Implement int sqrt(int x).

// Compute and return the square root of x, where x is guaranteed to be a non-negative integer.

// Since the return type is an integer, the decimal digits are truncated and only the integer part of the result is returned.

// Example 1:

// Input: 4
// Output: 2
// Example 2:

// Input: 8
// Output: 2
// Explanation: The square root of 8 is 2.82842..., and since
// the decimal part is truncated, 2 is returned.

// @lc code=start
func mySqrt(x int) int {
	// Accepted
	// 1017/1017 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 99.7 % of golang submissions (2.2 MB)
	if x == 0 || x == 1 {
		return x
	}
	var guess float64 = (2.0 / float64(x)) * float64(x)
	temp := 0
	for true {
		guess = (guess + float64(x)/guess) / 2
		t := int(guess)
		if temp == t {
			break
		} else {
			temp = t
		}
	}
	return temp
}

// @lc code=end
