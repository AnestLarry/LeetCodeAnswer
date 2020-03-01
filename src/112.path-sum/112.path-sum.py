#
# @lc app=leetcode id=112 lang=python3
#
# [112] Path Sum
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \      \
# 7    2      1
# return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
# √ Accepted
#   √ 114/114 cases passed (52 ms)
#   √ Your runtime beats 62.15 % of python3 submissions
#   √ Your memory usage beats 5.45 % of python3 submissions (15.6 MB)


class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        # Accepted
        # 114/114 cases passed (40 ms)
        # Your runtime beats 94.95 % of python3 submissions
        # Your memory usage beats 23.16 % of python3 submissions (15.6 MB)
        if not root:
            return False
        if not root.left and not root.right:
            if root.val == sum:
                return True

        if root.left:
            if self.hasPathSum(root.left, sum-root.val):
                return True
        if root.right:
            if self.hasPathSum(root.right, sum-root.val):
                return True
        return False
