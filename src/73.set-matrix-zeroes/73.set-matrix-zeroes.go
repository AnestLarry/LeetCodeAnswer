/*
 * @lc app=leetcode.cn id=73 lang=golang
 *
 * [73] Set Matrix Zeroes
 */
//  Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

// Example 1:

// Input:
// [
//   [1,1,1],
//   [1,0,1],
//   [1,1,1]
// ]
// Output:
// [
//   [1,0,1],
//   [0,0,0],
//   [1,0,1]
// ]
// Example 2:

// Input:
// [
//   [0,1,2,0],
//   [3,4,5,2],
//   [1,3,1,5]
// ]
// Output:
// [
//   [0,0,0,0],
//   [0,4,5,0],
//   [0,3,1,0]
// ]
// Follow up:

// A straight forward solution using O(mn) space is probably a bad idea.
// A simple improvement uses O(m + n) space, but still not the best solution.
// Could you devise a constant space solution?

// @lc code=start
func setZeroes(matrix [][]int) {
	// Accepted
	// 159/159 cases passed (12 ms)
	// Your runtime beats 97.7 % of golang submissions
	// Your memory usage beats 88.89 % of golang submissions (6 MB)
	ml, l := len(matrix), len(matrix[0])
	z := make([][]int, 0)
	for i := 0; i < ml; i++ {
		for j := 0; j < l; j++ {
			if matrix[i][j] == 0 {
				z = append(z, []int{i, j})
			}
		}
	}
	// Readable Code
	// Accepted
	// 159/159 cases passed (12 ms)
	// Your runtime beats 97.7 % of golang submissions
	// Your memory usage beats 86.42 % of golang submissions (6 MB)
	// if len(z) != 0 {
	// 	for i := 0; i < len(z); i++ {
	// 		for j := 0; j < l; j++ {
	// 			matrix[z[i][0]][j] = 0
	// 		}
	// 		for j := 0; j < ml; j++ {
	// 			matrix[j][z[i][1]] = 0
	// 		}
	// 	}
	// }
	zl := len(z)
	if zl != 0 {
		if l > ml {
			for i := 0; i < zl; i++ {
				j := 0
				for ; j < ml; j++ {
					matrix[z[i][0]][j] = 0
					matrix[j][z[i][1]] = 0
				}
				for ; j < l; j++ {
					matrix[z[i][0]][j] = 0
				}

			}
		} else {
			for i := 0; i < zl; i++ {
				j := 0
				for ; j < l; j++ {
					matrix[z[i][0]][j] = 0
					matrix[j][z[i][1]] = 0
				}
				for ; j < ml; j++ {
					matrix[j][z[i][1]] = 0
				}
			}
		}

	}

}

// @lc code=end
