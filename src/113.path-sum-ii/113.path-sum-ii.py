#
# @lc app=leetcode id=113 lang=python3
#
# [113] Path Sum II
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
# Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.

# Note: A leaf is a node with no children.

# Example:

# Given the below binary tree and sum = 22,

#       5
#      / \
#     4   8
#    /   / \
#   11  13  4
#  /  \    / \
# 7    2  5   1
# Return:

# [
#    [5,4,11,2],
#    [5,8,4,5]
# ]


class Solution:
    def pathSum(self, root: TreeNode, s: int) -> List[List[int]]:
        # Accepted
        # 114/114 cases passed (48 ms)
        # Your runtime beats 80.75 % of python3 submissions
        # Your memory usage beats 73.05 % of python3 submissions (14.5 MB)
        if not root:
            return []
        res = []
        stack = [(root, [root.val])]
        while stack:
            cur, ls = stack.pop()
            if not cur.left and not cur.right and sum(ls) == s:
                res.append(ls)
            if cur.right:
                stack.append((cur.right, ls+[cur.right.val]))
            if cur.left:
                stack.append((cur.left, ls+[cur.left.val]))
        return res
