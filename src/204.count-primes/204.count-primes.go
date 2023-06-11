import "math"

/*
 * @lc app=leetcode.cn id=204 lang=golang
 *
 * [204] Count Primes
 */
//  Count the number of prime numbers less than a non-negative number, n.

//  Example:

//  Input: 10
//  Output: 4
//  Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.

// @lc code=start
func countPrimes(n int) int {
	// Accepted
	// 20/20 cases passed (8 ms)
	// Your runtime beats 94.53 % of golang submissions
	// Your memory usage beats 28.37 % of golang submissions (4.9 MB)
	if n < 2 {
		return 0
	}
	res := make([]bool, n)
	for i, _ := range res {
		res[i] = true
	}
	res[0] = false
	res[1] = false
	for i := 0; i < (int)(math.Sqrt((float64)(n))+1); i++ {
		if res[i] {
			for j := i + i; j < n; j += i {
				res[j] = false
			}
		}
	}
	s := 0
	for i := 0; i < len(res); i++ {
		if res[i] {
			s += 1
		}
	}
	return s
}

// @lc code=end
