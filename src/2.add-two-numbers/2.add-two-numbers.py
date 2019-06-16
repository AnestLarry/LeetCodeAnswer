#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

# Example:

# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
# √ Accepted
#   √ 1563/1563 cases passed (72 ms)
#   √ Your runtime beats 94.88 % of python3 submissions
#   √ Your memory usage beats 58.5 % of python3 submissions (13.2 MB)
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        n,a=root,False
        while l1 and l2 :
            if a:
                r = l1.val+l2.val+1
                a=False
            else:
                r=l1.val+l2.val
            if r <10:
                n.next = ListNode(r)
            else:
                n.next = ListNode(r%10)
                a=True
            l1,l2,n=l1.next,l2.next,n.next
        while True:
            if l1:
                if a:
                    r = l1.val+1
                    a=False
                else:
                    r=l1.val
                if r<10:
                    n.next = ListNode(r)
                else:
                    n.next = ListNode(r%10)
                    a=True
                l1,n=l1.next,n.next
                continue
            elif l2:
                if a:
                    r = l2.val+1
                    a=False
                else:
                    r=l2.val
                if r<10:
                    n.next = ListNode(r)
                else:
                    n.next = ListNode(r%10)
                    a=True
                l2,n=l2.next,n.next
                continue
            elif a:
                n.next=ListNode(1)
                a=False
            break
        return root.next
