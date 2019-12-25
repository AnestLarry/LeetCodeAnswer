/*
 * @lc app=leetcode id=35 lang=golang
 *
 * [35] Search Insert Position
 */
//  Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

// You may assume no duplicates in the array.

// Example 1:

// Input: [1,3,5,6], 5
// Output: 2
// Example 2:

// Input: [1,3,5,6], 2
// Output: 1
// Example 3:

// Input: [1,3,5,6], 7
// Output: 4
// Example 4:

// Input: [1,3,5,6], 0
// Output: 0
func searchInsert(nums []int, target int) int {
	// Accepted
	// 62/62 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 58.73 % of golang submissions (3.1 MB)
	i, l := 0, len(nums)
	for i < l {
		if nums[i] >= target {
			return i
		}
		i += 1
	}
	return l
}

func searchInsert2(nums []int, target int) int {
	// Accepted
	// 62/62 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 55.95 % of golang submissions (3.1 MB)
	left, right := 0, len(nums)-1
	for left <= right {
		mid := (left + right) >> 1
		if nums[mid] == target {
			return mid
		}
		if nums[mid] < target {
			left = mid + 1
		} else {
			right = mid - 1
		}
	}
	return left
}
