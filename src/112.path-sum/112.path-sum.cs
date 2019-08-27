/*
 * @lc app=leetcode id=112 lang=csharp
 *
 * [112] Path Sum
 */
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
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
//  √ Accepted
//   √ 114/114 cases passed (104 ms)
//   √ Your runtime beats 69.65 % of csharp submissions
//   √ Your memory usage beats 91.67 % of csharp submissions (24.1 MB)
public class Solution
{
    public bool HasPathSum(TreeNode root, int sum)
    {
        if (root == null)
        {
            return false;
        }
        if (root.left == null && root.right == null)
        {
            if (root.val == sum)
            {
                return true;
            }
        }
        if (root.left != null)
        {
            if (HasPathSum(root.left, sum - root.val))
            {
                return true;
            }
        }
        if (root.right != null)
        {
            if (HasPathSum(root.right, sum - root.val))
            {
                return true;
            }
        }
        return false;
    }
}

