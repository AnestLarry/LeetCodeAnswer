#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
# With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list
# Algorithm of Insertion Sort:

# Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
# At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
# It repeats until no input elements remain.

# Example 1:

# Input: 4->2->1->3
# Output: 1->2->3->4
# Example 2:

# Input: -1->5->3->4->0
# Output: -1->0->3->4->5

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    def insertionSortList(self, head):
        # Accepted
        # 22/22 cases passed (116 ms)
        # Your runtime beats 94.53 % of python3 submissions
        # Your memory usage beats 8.47 % of python3 submissions (15.5 MB)
        p = dummy = ListNode(0)
        cur = dummy.next = head
        while cur and cur.next:
            val = cur.next.val
            if cur.val < val:
                cur = cur.next
                continue
            if p.next.val > val:
                p = dummy
            while p.next.val < val:
                p = p.next
            new = cur.next
            cur.next = new.next
            new.next = p.next
            p.next = new
        return dummy.next

    def insertionSortList2(self, head: ListNode) -> ListNode:
        # Accepted
        # 22/22 cases passed (52 ms)
        # Your runtime beats 98.12 % of python3 submissions
        # Your memory usage beats 5.65 % of python3 submissions (16.2 MB)
        if not head:
            return head
        r = []
        while head:
            r.append(head.val)
            head = head.next
        r.sort()
        root = h = ListNode(r[0])
        for i in range(1, len(r)):
            t = ListNode(r[i])
            h.next = t
            h = h.next
        return root
