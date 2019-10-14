/*
 * @lc app=leetcode id=142 lang=csharp
 *
 * [142] Linked List Cycle II
 */

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
//  Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

// To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

// Note: Do not modify the linked list.

// Example 1:

// Input: head = [3,2,0,-4], pos = 1
// Output: tail connects to node index 1
// Explanation: There is a cycle in the linked list, where tail connects to the second node.
public class Solution
{
    public ListNode DetectCycle(ListNode head)
    {
        // Accepted
        // 16/16 cases passed (104 ms)
        // Your runtime beats 47.16 % of csharp submissions
        // Your memory usage beats 33.33 % of csharp submissions (25 MB)
        if (head == null || head.next == null)
        {
            return null;
        }
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null)
        {
            slow = slow.next;
            fast = fast.next.next;
            if (slow == fast)
            {
                break;
            }
        }
        if (fast == null || fast.next == null)
        {
            return null;
        }
        slow = head;
        while (slow != fast)
        {
            slow = slow.next;
            fast = fast.next;
        }
        return fast;
    }
}
// @lc code=end

