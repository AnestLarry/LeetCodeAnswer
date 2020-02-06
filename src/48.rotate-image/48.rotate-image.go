/*
 * @lc app=leetcode.cn id=48 lang=golang
 *
 * [48] Rotate Image
 */
// You are given an n x n 2D matrix representing an image.

// Rotate the image by 90 degrees (clockwise).

// Note:

// You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

// Example 1:

// Given input matrix =
// [
//   [1,2,3],
//   [4,5,6],
//   [7,8,9]
// ],

// rotate the input matrix in-place such that it becomes:
// [
//   [7,4,1],
//   [8,5,2],
//   [9,6,3]
// ]
// Example 2:

// Given input matrix =
// [
//   [ 5, 1, 9,11],
//   [ 2, 4, 8,10],
//   [13, 3, 6, 7],
//   [15,14,12,16]
// ],

// rotate the input matrix in-place such that it becomes:
// [
//   [15,13, 2, 5],
//   [14, 3, 4, 1],
//   [12, 6, 8, 9],
//   [16, 7,10,11]
// ]
// @lc code=start
func rotate(matrix [][]int) {
	// Accepted
	// 21/21 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (2.2 MB)
	n := len(matrix)
	for i := 0; i < n; i++ {
		for j := i; j < n; j++ {
			if matrix[j][i] != matrix[i][j] {
				matrix[j][i] ^= matrix[i][j]
				matrix[i][j] ^= matrix[j][i]
				matrix[j][i] ^= matrix[i][j]
			}
		}
	}
	for i := 0; i < n; i++ {
		for j := 0; j < n/2; j++ {
			tmp := n - j - 1
			if matrix[i][j] != matrix[i][tmp] {
				matrix[i][j] ^= matrix[i][tmp]
				matrix[i][tmp] ^= matrix[i][j]
				matrix[i][j] ^= matrix[i][tmp]
			}
		}
	}
}

// @lc code=end