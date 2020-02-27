/*
 * @lc app=leetcode.cn id=81 lang=golang
 *
 * [81] Search in Rotated Sorted Array II
 */
//  Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

// You are given a target value to search. If found in the array return true, otherwise return false.

// Example 1:

// Input: nums = [2,5,6,0,0,1,2], target = 0
// Output: true
// Example 2:

// Input: nums = [2,5,6,0,0,1,2], target = 3
// Output: false
// Follow up:

// This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
// Would this affect the run-time complexity? How and why?
// @lc code=start
func search(nums []int, target int) bool {
	// Accepted
	// 275/275 cases passed (4 ms)
	// Your runtime beats 95.7 % of golang submissions
	// Your memory usage beats 98.18 % of golang submissions (3.2 MB)
	l, r := 0, len(nums)-1
	if r < 0 {
		return false
	}
	for l <= r {
		mid := l + ((r - l) >> 1)
		if nums[mid] == target {
			return true
		}
		for l < mid && nums[l] == nums[mid] {
			l++
		}
		if nums[l] <= nums[mid] {
			if nums[l] <= target && target < nums[mid] {
				r = mid - 1
			} else {
				l = mid + 1
			}
		} else {
			if nums[mid] < target && target <= nums[r] {
				l = mid + 1
			} else {
				r = mid - 1
			}
		}
	}
	return false
}

// @lc code=end
