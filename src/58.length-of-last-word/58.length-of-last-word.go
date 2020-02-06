/*
 * @lc app=leetcode.cn id=58 lang=golang
 *
 * [58] Length of Last Word
 */
//  Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

// If the last word does not exist, return 0.

// Note: A word is defined as a character sequence consists of non-space characters only.

// Example:

// Input: "Hello World"
// Output: 5
// @lc code=start
func lengthOfLastWord(s string) int {
	// Accepted
	// 59/59 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 74.7 % of golang submissions (2.1 MB)
	r, res := len(s)-1, 0
	for r > -1 && s[r] == ' ' {
		r--
	}
	for r > -1 && s[r] != ' ' {
		r--
		res++
	}
	return res
}

// @lc code=end
