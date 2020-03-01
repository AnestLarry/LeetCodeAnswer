/*
 * @lc app=leetcode.cn id=113 lang=csharp
 *
 * [113] Path Sum II
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
public class Solution {
    public IList<IList<int>> PathSum (TreeNode root, int sum) {
        // Accepted
        // 114/114 cases passed (272 ms)
        // Your runtime beats 100 % of csharp submissions
        // Your memory usage beats 29.63 % of csharp submissions (32.4 MB)
        if (root == null) {
            return new List<IList<int>> ();
        }
        var res = new List<IList<int>> ();
        var stack = new Stack < (TreeNode Node, int Sum, int Index) > ();
        var path = new List<int> ();
        stack.Push ((root, root.val, 0));
        while (stack.Count != 0) {
            var p = stack.Pop ();
            TreeNode node = p.Node;
            int psum = p.Sum;
            int index = p.Index;

            if (index < path.Count)
                path[index] = node.val;
            else
                path.Add (node.val);

            if (node.right != null)
                stack.Push ((node.right, node.right.val + psum, index + 1));
            if (node.left != null)
                stack.Push ((node.left, node.left.val + psum, index + 1));

            if (node.right == null && node.left == null && psum == sum)
                res.Add (path.GetRange (0, index + 1));
        }
        return res;
    }
}
// @lc code=end