#
# @lc app=leetcode id=148 lang=python3
#
# [148] Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Sort a linked list in O(n log n) time using constant space complexity.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5
# √ Accepted
#   √ 16/16 cases passed (104 ms)
#   √ Your runtime beats 96.31 % of python3 submissions
#   √ Your memory usage beats 6.35 % of python3 submissions (25.6 MB)
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        lists = []
        while head:
            lists+=[head.val]
            head=head.next
        lists.sort()
        root = n =ListNode(0)
        for i in lists:
            n.next=ListNode(i)
            n=n.next
        return root.next
