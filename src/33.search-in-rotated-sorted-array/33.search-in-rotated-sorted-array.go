import "sort"

/*
 * @lc app=leetcode.cn id=33 lang=golang
 *
 * [33] Search in Rotated Sorted Array
 */
// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

// You are given a target value to search. If found in the array return its index, otherwise return -1.

// You may assume no duplicate exists in the array.

// Your algorithm's runtime complexity must be in the order of O(log n).

// Example 1:

// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4
// Example 2:

// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1
// @lc code=start
func search(nums []int, target int) int {
	// Accepted
	// 196/196 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 50.35 % of golang submissions (2.6 MB)
	l, i := len(nums), 1
	if l < 1 {
		return -1
	} else if l < 2 {
		if nums[0] == target {
			return 0
		} else {
			return -1
		}
	}

	for i = 0; i < l; i++ {
		if nums[i] < nums[0] {
			break
		}
	}
	sort.Ints(nums)
	result, left, right := -1, 0, l-1
	for left <= right {
		mid := (left + right) >> 1
		if nums[mid] == target {
			result = mid + i
			if result > l-1 && i != 0 {
				return result - l
			}
			return result
		}
		if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return result
}

// @lc code=end
