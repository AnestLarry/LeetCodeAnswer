#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

# Example:

# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Accepted
        # 208/208 cases passed (28 ms)
        # Your runtime beats 99.92 % of python3 submissions
        # Your memory usage beats 99.29 % of python3 submissions (12.8 MB)
        if not l1 or not l2:
            return l1 if l1 else l2
        root = ListNode(0)
        node = root
        while l1 and l2:
            if l1.val > l2.val:
                node.next = l2
                l2 = l2.next
            else:
                node.next = l1
                l1 = l1.next
            node = node.next
        if l1:
            node.next = l1
        else:
            node.next = l2
        return root.next
