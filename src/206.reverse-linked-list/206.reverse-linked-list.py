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
