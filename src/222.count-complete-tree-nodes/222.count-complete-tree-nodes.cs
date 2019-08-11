/*
 * @lc app=leetcode id=222 lang=csharp
 *
 * [222] Count Complete Tree Nodes
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
//  Given a complete binary tree, count the number of nodes.

// Note:

// Definition of a complete binary tree from Wikipedia:
// In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

// Example:

// Input: 
//     1
//    / \
//   2   3
//  / \  /
// 4  5 6

// Output: 6
//  √ Accepted
//   √ 18/18 cases passed (116 ms)
//   √ Your runtime beats 51.93 % of csharp submissions
//   √ Your memory usage beats 50 % of csharp submissions (30.6 MB)
public class Solution {
    public int CountNodes(TreeNode root) {
        if(root == null){
            return 0;
        }else{
            int res=1;
            if(root.left != null){
                res+=CountNodes(root.left);
            }
            if(root.right != null){
                res+=CountNodes(root.right);
            }
            return res;
        }
    }
}
