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


class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # Accepted
        # 16/16 cases passed (240 ms)
        # Your runtime beats 53.28 % of python3 submissions
        # Your memory usage beats 28.57 % of python3 submissions (20.6 MB)
        if not head or not head.next:
            return head
        slow = fast = head
        while fast.next and fast.next.next:
            slow, fast = slow.next, fast.next.next
        leftTail = slow
        slow = slow.next
        leftTail.next = None
        left, right = self.sortList(head), self.sortList(slow)
        return self.mergeLinked(left, right)

    def mergeLinked(self, left, right):
        temp = cur = ListNode(0)
        while left and right:
            if left.val < right.val:
                cur.next = left
                left = left.next
            else:
                cur.next = right
                right = right.next
            cur = cur.next
        if left:
            cur.next = left
        elif right:
            cur.next = right
        return temp.next

    def sortList2(self, head: ListNode) -> ListNode:
        # Accepted
        # 16/16 cases passed (92 ms)
        # Your runtime beats 96.37 % of python3 submissions
        # Your memory usage beats 7.14 % of python3 submissions (25.5 MB)
        lists = []
        while head:
            lists += [head.val]
            head = head.next
        lists.sort()
        root = n = ListNode(0)
        for i in lists:
            n.next = ListNode(i)
            n = n.next
        return root.next
