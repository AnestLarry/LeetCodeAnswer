import (
	"strconv"
)

/*
 * @lc app=leetcode id=9 lang=golang
 *
 * [9] Palindrome Number
 */
//  Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

// Example 1:

// Input: 121
// Output: true
// Example 2:

// Input: -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
// Follow up:

// Coud you solve it without converting the integer to a string?

func isPalindrome(x int) bool {
	// Accepted
	// 11509/11509 cases passed (8 ms)
	// Your runtime beats 98.06 % of golang submissions
	// Your memory usage beats 17.32 % of golang submissions (5.4 MB)
	if x < 0 {
		return false
	}
	xs := strconv.Itoa(x)
	l_xs := len(xs)
	var left string
	if l_xs%2 != 0 {
		left = xs[:int(l_xs/2)+1]
	} else {
		left = xs[:int(l_xs/2)]
	}
	right := xs[int(l_xs/2):]
	r_l := len(right) - 1
	for i := 0; i <= r_l; i++ {
		if left[r_l-i] != right[i] {
			return false
		}
	}
	return true

}

func isPalindrome2(x int) bool {
	// Accepted
	// 11509/11509 cases passed (24 ms)
	// Your runtime beats 45.67 % of golang submissions
	// Your memory usage beats 35.68 % of golang submissions (5.2 MB)
	if x < 0 {
		return false
	} else if x < 10 {
		return true
	}
	r, rx := 0, x
	for rx > 0 {
		r, rx = r*10+rx%10, int(rx/10)
	}
	if r == x {
		return true
	}
	return false
}
