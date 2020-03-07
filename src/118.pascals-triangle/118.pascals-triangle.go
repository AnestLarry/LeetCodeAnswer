/*
 * @lc app=leetcode.cn id=118 lang=golang
 *
 * [118] Pascal's Triangle
 */
// Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it.

// Example:

// Input: 5
// Output:
// [
//      [1],
//     [1,1],
//    [1,2,1],
//   [1,3,3,1],
//  [1,4,6,4,1]
// ]
// @lc code=start
func generate(numRows int) [][]int {
	// Accepted
	// 15/15 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 69.54 % of golang submissions (2 MB)
	if numRows < 1 {
		return [][]int{}
	}
	res := make([][]int, numRows)
	i := 0
	for i < numRows {
		res[i] = make([]int, i+1)
		res[i][0], res[i][i] = 1, 1
		j := 1
		for j < i {
			res[i][j] = res[i-1][j-1] + res[i-1][j]
			j++
		}
		i++
	}
	return res
}

// @lc code=end
