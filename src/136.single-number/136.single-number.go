/*
 * @lc app=leetcode.cn id=136 lang=golang
 *
 * [136] 只出现一次的数字
 */
/*
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
*/
// @lc code=start
func singleNumber(nums []int) int {
	// Accepted
	// 16/16 cases passed (8 ms)
	// Your runtime beats 98.61 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (4.7 MB)	r := nums[0]
	r := nums[0]
	for i := 1; i < len(nums); i++ {
		r ^= nums[i]
	}
	return r
}

// @lc code=end
