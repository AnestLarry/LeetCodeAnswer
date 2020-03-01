/*
 * @lc app=leetcode.cn id=113 lang=golang
 *
 * [113] Path Sum II
 */
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
// Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

// Note: A leaf is a node with no children.

// Example:

// Given the below binary tree and sum = 22,

//       5
//      / \
//     4   8
//    /   / \
//   11  13  4
//  /  \    / \
// 7    2  5   1
// Return:

// [
//    [5,4,11,2],
//    [5,8,4,5]
// ]
// @lc code=start

func pathSum(root *TreeNode, sum int) [][]int {
	// Accepted
	// 114/114 cases passed (4 ms)
	// Your runtime beats 94.29 % of golang submissions
	// Your memory usage beats 30.67 % of golang submissions (6.3 MB)
	if root == nil {
		return nil
	}

	var res [][]int
	if root.Left == nil && root.Right == nil {
		if sum == root.Val {
			return append(res, []int{root.Val})
		}
		return res
	}
	sum -= root.Val
	for _, path := range pathSum(root.Left, sum) {
		res = append(res, append([]int{root.Val}, path...))
	}
	for _, path := range pathSum(root.Right, sum) {
		res = append(res, append([]int{root.Val}, path...))
	}
	return res
}

// @lc code=end
