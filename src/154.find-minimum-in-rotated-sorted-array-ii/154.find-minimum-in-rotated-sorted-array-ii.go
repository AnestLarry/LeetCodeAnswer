/*
 * @lc app=leetcode.cn id=154 lang=golang
 *
 * [154] Find Minimum in Rotated Sorted Array II
 */
//  Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

// Find the minimum element.

// The array may contain duplicates.

// Example 1:

// Input: [1,3,5]
// Output: 1
// Example 2:

// Input: [2,2,2,0,1]
// Output: 0
// Note:

// This is a follow up problem to Find Minimum in Rotated Sorted Array.
// Would allow duplicates affect the run-time complexity? How and why?
// @lc code=start
func findMin(nums []int) int {
	// Accepted
	// 192/192 cases passed (4 ms)
	// Your runtime beats 92.91 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (3.1 MB)
	l := len(nums)
	if l < 2 {
		return nums[0]
	}
	last, i := l-1, l-2
	for i > -1 && nums[i] <= nums[last] {
		if nums[i>>1] < nums[last] {
			last = i >> 1
			i = last - 1
		} else {
			last = i
			i--
		}
	}
	return nums[last]
}

// @lc code=end
