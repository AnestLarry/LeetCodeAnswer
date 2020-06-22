/*
 * @lc app=leetcode.cn id=153 lang=golang
 *
 * [153] Find Minimum in Rotated Sorted Array
 */
//  Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

// Find the minimum element.

// You may assume no duplicate exists in the array.

// Example 1:

// Input: [3,4,5,1,2]
// Output: 1
// Example 2:

// Input: [4,5,6,7,0,1,2]
// Output: 0
// @lc code=start
func findMin(nums []int) int {
	// Accepted
	// 146/146 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 57.14 % of golang submissions (2.5 MB)
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
