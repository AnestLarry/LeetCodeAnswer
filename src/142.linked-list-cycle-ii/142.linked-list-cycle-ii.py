#
# @lc app=leetcode id=142 lang=python3
#
# [142] Linked List Cycle II
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Note: Do not modify the linked list.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: tail connects to node index 1
# Explanation: There is a cycle in the linked list, where tail connects to the second node.


class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        # Accepted
        # 16/16 cases passed (52 ms)
        # Your runtime beats 85.48 % of python3 submissions
        # Your memory usage beats 5.13 % of python3 submissions (16.7 MB)
        if not head or not head.next:
            return None
        slow = fast = head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
            if slow == fast:
                break
        if not fast or not fast.next:
            return None
        while head != fast:
            head, fast = head.next, fast.next
        return fast
# @lc code=end
