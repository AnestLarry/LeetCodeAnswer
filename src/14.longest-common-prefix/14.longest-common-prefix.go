/*
 * @lc app=leetcode.cn id=14 lang=golang
 *
 * [14] Longest Common Prefix
 */

//  Write a function to find the longest common prefix string amongst an array of strings.

// If there is no common prefix, return an empty string "".

// Example 1:

// Input: ["flower","flow","flight"]
// Output: "fl"
// Example 2:

// Input: ["dog","racecar","car"]
// Output: ""
// Explanation: There is no common prefix among the input strings.
// Note:

// All given inputs are in lowercase letters a-z.

// @lc code=start
func longestCommonPrefix(strs []string) string {
	// Accepted
	// 118/118 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 61.56 % of golang submissions (2.4 MB)
	if strs == nil || len(strs) < 2 {
		if len(strs) == 1 {
			return strs[0]
		}
		return ""
	}
	pre_num := len(strs[0])
	for {
		flag := true
		for i := 1; i < len(strs); i++ {
			if pre_num == 0 {
				return ""
			}
			if len(strs[i]) < pre_num || strs[i][:pre_num] != strs[i-1][:pre_num] {
				pre_num--
				flag = false
				break
			}
		}
		if flag {
			break
		} else {
			flag = true
		}
	}

	return strs[0][:pre_num]
}

// @lc code=end
