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
# √ Accepted
#   √ 208/208 cases passed (40 ms)
#   √ Your runtime beats 91.74 % of python3 submissions
#   √ Your memory usage beats 50.45 % of python3 submissions (13.2 MB)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if not l1 or not l2:
            if l1:
                return l1
            elif l2:
                return l2
            return None
        root=ListNode(0)
        node=root
        while l1 and l2:
            if l1.val > l2.val:
                node.next =l2
                l2=l2.next
            else:
                node.next =l1
                l1=l1.next
            node=node.next
        if l1:
            node.next=l1
        else:
            node.next=l2
        return root.next
        


