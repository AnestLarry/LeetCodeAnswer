#
# @lc app=leetcode id=222 lang=python3
#
# [222] Count Complete Tree Nodes
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Given a complete binary tree, count the number of nodes.

# Note:

# Definition of a complete binary tree from Wikipedia:
# In a complete binary tree every level, except possibly the last, is completely filled, and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes inclusive at the last level h.

# Example:

# Input: 
#     1
#    / \
#   2   3
#  / \  /
# 4  5 6

# Output: 6
# √ Accepted
#   √ 18/18 cases passed (100 ms)
#   √ Your runtime beats 45.94 % of python3 submissions
#   √ Your memory usage beats 6.9 % of python3 submissions (21.6 MB)
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        else:
            res=1
            if root.left:
                res+=self.countNodes(root.left)
            if root.right:
                res+=self.countNodes(root.right)
            return res


