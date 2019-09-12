#
# @lc app=leetcode id=147 lang=python3
#
# [147] Insertion Sort List
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
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
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        # √ Accepted
        #   √ 22/22 cases passed (60 ms)
        #   √ Your runtime beats 97.69 % of python3 submissions
        #   √ Your memory usage beats 25 % of python3 submissions (16.6 MB)
        if not head:
            return head
        r = []
        while head:
            r.append(head.val)
            head=head.next
        r.sort()
        root = h = ListNode(r[0])
        for i in range(1,len(r)):
            t=ListNode(r[i])
            h.next = t
            h=h.next
        return root

