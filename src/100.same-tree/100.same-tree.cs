/*
 * @lc app=leetcode id=100 lang=csharp
 *
 * [100] Same Tree
 */

// @lc code=start
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     public int val;
 *     public TreeNode left;
 *     public TreeNode right;
 *     public TreeNode(int x) { val = x; }
 * }
 */
//  Given two binary trees, write a function to check if they are the same or not.

// Two binary trees are considered the same if they are structurally identical and the nodes have the same value.

// Example 1:

// Input:     1         1
//           / \       / \
//          2   3     2   3

//         [1,2,3],   [1,2,3]

// Output: true
// Example 2:

// Input:     1         1
//           /           \
//          2             2

//         [1,2],     [1,null,2]

// Output: false
// Example 3:

// Input:     1         1
//           / \       / \
//          2   1     1   2

//         [1,2,1],   [1,1,2]

// Output: false
public class Solution {
    public bool IsSameTree (TreeNode p, TreeNode q) {
        // Accepted
        // 57/57 cases passed (104 ms)
        // Your runtime beats 91.82 % of csharp submissions
        // Your memory usage beats 7.24 % of csharp submissions (24.1 MB)
        if (p == null || q == null) {
            return p == null && q == null;
        } else {
            return p.val == q.val && IsSameTree (p.left, q.left) && IsSameTree (p.right, q.right);
        }
    }
}
// @lc code=end