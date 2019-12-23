/*
 * @lc app=leetcode.cn id=28 lang=golang
 *
 * [28] Implement strStr()
 */
//  Implement strStr().

// Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

// Example 1:

// Input: haystack = "hello", needle = "ll"
// Output: 2
// Example 2:

// Input: haystack = "aaaaa", needle = "bba"
// Output: -1
// Clarification:

// What should we return when needle is an empty string? This is a great question to ask during an interview.

// For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().
// @lc code=start
func strStr(haystack string, needle string) int {
	// Accepted
	// 74/74 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 69.03 % of golang submissions (2.3 MB)
	if needle == "" {
		return 0
	}
	nl := len(needle)
	for i := 0; i < len(haystack)-nl+1; i++ {
		if haystack[i:i+nl] == needle {
			return i
		}
	}
	return -1
}

// @lc code=end
