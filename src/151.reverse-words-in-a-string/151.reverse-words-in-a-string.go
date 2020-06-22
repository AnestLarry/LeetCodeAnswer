import "strings"

/*
 * @lc app=leetcode.cn id=151 lang=golang
 *
 * [151] Reverse Words in a String
 */
/*
 Given an input string, reverse the string word by word.


Example 1:

Input: "the sky is blue"
Output: "blue is sky the"
Example 2:

Input: "  hello world!  "
Output: "world! hello"
Explanation: Your reversed string should not contain leading or trailing spaces.
Example 3:

Input: "a good   example"
Output: "example good a"
Explanation: You need to reduce multiple spaces between two words to a single space in the reversed string.


Note:

A word is defined as a sequence of non-space characters.
Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
You need to reduce multiple spaces between two words to a single space in the reversed string.


Follow up:

For C programmers, try to solve it in-place in O(1) extra space.
*/
// @lc code=start
func reverseWords(s string) string {
	// Accepted
	// 25/25 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (3.7 MB)
	sl := strings.Split(strings.Trim(s, " "), " ")
	res := make([]string, 0)
	for i := len(sl) - 1; i > -1; i-- {
		if len(sl[i]) > 0 {
			res = append(res, strings.Trim(sl[i], " "))
		}
	}
	return strings.Join(res, " ")
}

// @lc code=end

