/*
 * @lc app=leetcode id=41 lang=golang
 *
 * [41] First Missing Positive
 */
/*Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.*/
// @lc code=start
func firstMissingPositive(nums []int) int {
	// Accepted
	// 165/165 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 79.37 % of golang submissions (2.2 MB)
	for i := 1; i < len(nums)+2; i++ {
		if Finder(nums, i) == false {
			return i
		}
	}
	return 1
}
func Finder(nums []int, target int) bool {
	for _, v := range nums {
		if v == target {
			return true
		}
	}
	return false
}

// @lc code=end
