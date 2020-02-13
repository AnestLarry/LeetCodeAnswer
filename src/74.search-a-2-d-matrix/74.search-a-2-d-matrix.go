/*
 * @lc app=leetcode.cn id=74 lang=golang
 *
 * [74] Search a 2D Matrix
 */
//  Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

// Integers in each row are sorted from left to right.
// The first integer of each row is greater than the last integer of the previous row.
// Example 1:

// Input:
// matrix = [
//   [1,   3,  5,  7],
//   [10, 11, 16, 20],
//   [23, 30, 34, 50]
// ]
// target = 3
// Output: true
// Example 2:

// Input:
// matrix = [
//   [1,   3,  5,  7],
//   [10, 11, 16, 20],
//   [23, 30, 34, 50]
// ]
// target = 13
// Output: false
// @lc code=start
func searchMatrix(matrix [][]int, target int) bool {
	// Accepted
	// 136/136 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (3.8 MB)
	if len(matrix) == 0 || len(matrix[0]) == 0 {
		return false
	}
	l, ll, left := len(matrix)-1, len(matrix[0])-1, 0
	if target < matrix[0][0] || target > matrix[l][ll] {
		return false
	}
	for left < l {
		mid := (left + l) >> 1
		if matrix[mid][ll] == target {
			return true
		} else if matrix[mid][ll] > target {
			l = mid
		} else {
			left = mid + 1
		}
	}
	left = 0
	for left <= ll {
		mid := (left + ll) >> 1
		if matrix[l][mid] == target {
			return true
		} else if matrix[l][mid] < target {
			left = mid + 1
		} else {
			ll = mid - 1
		}
	}
	return false
}

// @lc code=end
