/*
 * @lc app=leetcode id=141 lang=csharp
 *
 * [141] Linked List Cycle
 */
//  Given a linked list, determine if it has a cycle in it.

// To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

// Example 1:

// Input: head = [3,2,0,-4], pos = 1
// Output: true
// Explanation: There is a cycle in the linked list, where tail connects to the second node.

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) {
 *         val = x;
 *         next = null;
 *     }
 * }
 */
public class Solution {
    public bool HasCycle (ListNode head) {
        // Accepted
        // 17/17 cases passed (104 ms)
        // Your runtime beats 97.98 % of csharp submissions
        // Your memory usage beats 9.26 % of csharp submissions (25.7 MB)
        if (head == null || head.next == null) {
            return false;
        }
        ListNode root = head.next;
        ListNode temp;
        while (root != null) {
            if (root.next == head) {
                return true;
            }
            temp = root.next;
            root.next = head;
            root = temp;
        }
        return false;
    }
}
// @lc code=end