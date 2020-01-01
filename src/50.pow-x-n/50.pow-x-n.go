/*
 * @lc app=leetcode.cn id=50 lang=golang
 *
 * [50] Pow(x, n)
Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]

*/

// @lc code=start
func myPow(x float64, n int) float64 {
	// Accepted
	// 304/304 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 61.97 % of golang submissions (2 MB)
	m := n < 0
	p := 1.0
	for n != 0 {
		if (n & 1) == 1 {
			p *= x
		}
		x *= x
		n /= 2
	}
	if m {
		return 1 / p
	} else {
		return p
	}
}

func myPow2(x float64, n int) float64 {
	// Accepted
	// 304/304 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 61.97 % of golang submissions (2 MB)
	if n == 0 {
		return 1
	}
	if n == 1 {
		return x
	}
	if n < 0 {
		return 1 / myPow(x, -n)
	}
	if n == 2 {
		return x * x
	}
	if n%2 == 0 {
		return myPow(x*x, n/2)
	} else {
		return x * myPow(x, n-1)
	}
}

// @lc code=end
