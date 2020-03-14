/*
 * @lc app=leetcode.cn id=139 lang=golang
 *
 * [139] Word Break
 */
/*Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
*/
// @lc code=start
func wordBreak(s string, wordDict []string) bool {
	// Accepted
	// 36/36 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 95.19 % of golang submissions (2.1 MB)
	if wordDict == nil {
		if s != "" {
			return false
		} else {
			return true
		}
	}

	l := len(s)
	bl := make([]bool, l+1)
	bl[0] = true
	for i := 1; i <= l; i++ {
		bl[i] = false
		for j := i - 1; j > -1; j-- {
			if bl[j] && StringsContains(wordDict, s[j:i]) != -1 {
				bl[i] = true
				break
			}
		}
	}
	return bl[l]
}

func StringsContains(array []string, val string) (index int) {
	index = -1
	for i := 0; i < len(array); i++ {
		if array[i] == val {
			index = i
			return
		}
	}
	return
}

// @lc code=end
