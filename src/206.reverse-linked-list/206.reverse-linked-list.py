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
# √ Accepted
#   √ 27/27 cases passed (44 ms)
#   √ Your runtime beats 51.68 % of python3 submissions
#   √ Your memory usage beats 40.39 % of python3 submissions (14.6 MB)
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre,cur = head,head.next
        while cur:
            temp=cur.next
            cur.next=pre
            pre = cur
            cur = temp
        head.next=None
        return pre
