/*
 * @lc app=leetcode.cn id=119 lang=golang
 *
 * [119] Pascal's Triangle II
 */
//  Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

//  Note that the row index starts from 0.

//  In Pascal's triangle, each number is the sum of the two numbers directly above it.

//  Example:

//  Input: 3
//  Output: [1,3,3,1]
//  Follow up:

//  Could you optimize your algorithm to use only O(k) extra space?

// @lc code=start
func getRow(rowIndex int) []int {
	// Accepted
	// 34/34 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 88.33 % of golang submissions (2 MB)
	res := make([]int, rowIndex+1)
	for i := 0; i <= rowIndex; i++ {
		res[i] = 1
		for j := i; j > 1; j-- {
			res[j-1] = res[j-1] + res[j-2]
		}
	}
	return res
}

// @lc code=end
