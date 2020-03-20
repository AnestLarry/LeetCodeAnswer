#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] Linked List Cycle
#
#  Given a linked list, determine if it has a cycle in it.

# To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

# Example 1:

# Input: head = [3,2,0,-4], pos = 1
# Output: true
# Explanation: There is a cycle in the linked list, where tail connects to the second node.

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # Accepted
        # 17/17 cases passed (48 ms)
        # Your runtime beats 91.07 % of python3 submissions
        # Your memory usage beats 99.42 % of python3 submissions (15 MB)
        if head == None or head.next == None:
            return False
        root = head.next
        while root != None:
            if root.next == head:
                return True

            temp = root.next
            root.next = head
            root = temp
        return False
# @lc code=end
