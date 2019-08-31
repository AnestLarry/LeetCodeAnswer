#
# @lc app=leetcode id=206 lang=python3
#
# [206] Reverse Linked List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# Reverse a singly linked list.

# Example:

# Input: 1->2->3->4->5->NULL
# Output: 5->4->3->2->1->NULL
# Follow up:

# A linked list can be reversed either iteratively or recursively. Could you implement both?
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # √ Accepted
        #   √ 27/27 cases passed (32 ms)
        #   √ Your runtime beats 99.56 % of python3 submissions
        #   √ Your memory usage beats 31.82 % of python3 submissions (15.1 MB)
        if not head or not head.next:
            return head
        pre, cur = head, head.next
        while cur:
            ne, cur.next = cur.next, pre
            pre, cur = cur, ne
        head.next = None
        return pre
