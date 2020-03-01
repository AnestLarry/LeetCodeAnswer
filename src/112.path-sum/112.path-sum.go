/*
 * @lc app=leetcode.cn id=112 lang=golang
 *
 * [112] 路径总和
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * type TreeNode struct {
 *     Val int
 *     Left *TreeNode
 *     Right *TreeNode
 * }
 */
//  Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

// Note: A leaf is a node with no children.

// Example:

// Given the below binary tree and sum = 22,

//       5
//      / \
//     4   8
//    /   / \
//   11  13  4
//  /  \      \
// 7    2      1
// return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
func hasPathSum(root *TreeNode, sum int) bool {
	// Accepted
	// 114/114 cases passed (4 ms)
	// Your runtime beats 97 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (4.8 MB)
	if root == nil {
		return false
	}
	if root.Val == sum && root.Left == nil && root.Right == nil {
		return true
	}
	if root.Left == nil && root.Right == nil {
		return false
	}
	sum -= root.Val
	return hasPathSum(root.Left, sum) || hasPathSum(root.Right, sum)

}

// @lc code=end
