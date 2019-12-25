/*
 * @lc app=leetcode.cn id=34 lang=golang
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */
// Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

// Your algorithm's runtime complexity must be in the order of O(log n).

// If the target is not found in the array, return [-1, -1].

// Example 1:

// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]
// Example 2:

// Input: nums = [5,7,7,8,8,10], target = 6
// Output: [-1,-1]
// @lc code=start
func searchRange(nums []int, target int) []int {
	// Accepted
	// 88/88 cases passed (8 ms)
	// Your runtime beats 92.81 % of golang submissions
	// Your memory usage beats 60.76 % of golang submissions (4.1 MB)
	first, last, l := -1, -1, len(nums)
	if l < 1 {
		return []int{-1, -1}
	}

	for i := 0; i < l; i++ {
		if nums[i] < target {
			continue
		} else if nums[i] == target {
			first, last = i, i
			for ; i < l; i++ {
				if nums[i] == nums[first] {
					last = i
				} else {
					return []int{first, last}
				}
			}
		}
		break
	}
	return []int{first, last}
}

// @lc code=end
