/*
 * @lc app=leetcode.cn id=67 lang=golang
 *
 * [67] Add Binary
 */
// Given two binary strings, return their sum (also a binary string).

// The input strings are both non-empty and contains only characters 1 or 0.

// Example 1:

// Input: a = "11", b = "1"
// Output: "100"
// Example 2:

// Input: a = "1010", b = "1011"
// Output: "10101"

// @lc code=start
func addBinary(a string, b string) string {
	// Accepted
	// 294/294 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 21.03 % of golang submissions (2.7 MB)
	if len(a) > len(b) {
		for len(a) > len(b) {
			b = "0" + b
		}
	} else {
		for len(a) < len(b) {
			a = "0" + a
		}
	}

	res := ""
	flag := false
	for i := len(a) - 1; -1 < i; i-- {
		if a[i] == b[i] {
			if a[i] == '0' {
				if flag {
					res = "1" + res
				} else {
					res = "0" + res
				}
				flag = false

			} else {
				if flag {
					res = "1" + res
				} else {
					res = "0" + res
				}
				flag = true
			}

		} else {
			if flag {
				res = "0" + res
			} else {
				res = "1" + res
			}
		}
	}
	if flag {
		res = "1" + res
	}
	return res
}

// @lc code=end
