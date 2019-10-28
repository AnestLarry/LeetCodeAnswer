#
# @lc app=leetcode id=237 lang=python3
#
# [237] Delete Node in a Linked List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Write a function to delete a node (except the tail) in a singly linked list, given only access to that node.

# Given linked list -- head = [4,5,1,9], which looks like following:

# Example 1:

# Input: head = [4,5,1,9], node = 5
# Output: [4,1,9]
# Explanation: You are given the second node with value 5, the linked list should become 4 -> 1 -> 9 after calling your function.
# Example 2:

# Input: head = [4,5,1,9], node = 1
# Output: [4,5,9]
# Explanation: You are given the third node with value 1, the linked list should become 4 -> 5 -> 9 after calling your function.


# Note:

# The linked list will have at least two elements.
# All of the nodes' values will be unique.
# The given node will not be the tail and it will always be a valid node of the linked list.
# Do not return anything from your function.
class Solution:
    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Accepted
        # 41/41 cases passed (40 ms)
        # Your runtime beats 94.43 % of python3 submissions
        # Your memory usage beats 9.38 % of python3 submissions (14 MB)
        node.val, node.next = node.next.val, node.next.next
# @lc code=end
