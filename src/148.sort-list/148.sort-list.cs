/*
 * @lc app=leetcode id=148 lang=csharp
 *
 * [148] Sort List
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
//  Sort a linked list in O(n log n) time using constant space complexity.

// Example 1:

// Input: 4->2->1->3
// Output: 1->2->3->4
// Example 2:

// Input: -1->5->3->4->0
// Output: -1->0->3->4->5
public class Solution {
    public ListNode SortList (ListNode head) {
        // Accepted
        // 16/16 cases passed (120 ms)
        // Your runtime beats 100 % of csharp submissions
        // Your memory usage beats 100 % of csharp submissions (30.1 MB)
        if (head == null || head.next == null) {
            return head;
        }
        ListNode slow = head, fast = head, leftTail, left, right;
        while (fast.next != null && fast.next.next != null) {
            slow = slow.next;
            fast = fast.next.next;
        }
        leftTail = slow;
        slow = slow.next;
        leftTail.next = null;

        left = SortList (head);
        right = SortList (slow);
        return mergeLinked (left, right);
    }
    public ListNode mergeLinked (ListNode left, ListNode right) {
        ListNode cur = new ListNode (0), temp = cur;
        while (left != null && right != null) {
            if (left.val < right.val) {
                cur.next = left;
                left = left.next;
            } else {
                cur.next = right;
                right = right.next;
            }
            cur = cur.next;
        }
        if (left != null) {
            cur.next = left;
        } else if (right != null) {
            cur.next = right;
        }
        return temp.next;
    }

    public ListNode SortList2 (ListNode head) {
        // Accepted
        // 16/16 cases passed (124 ms)
        // Your runtime beats 96.88 % of csharp submissions
        // Your memory usage beats 100 % of csharp submissions (31.5 MB)
        List<int> lists = new List<int> ();
        while (head != null) {
            lists.Add (head.val);
            head = head.next;
        }
        lists.Sort ();
        ListNode root = new ListNode (0);
        ListNode n = root;
        for (int i = 0; i < lists.Count; i++) {
            n.next = new ListNode (lists[i]);
            n = n.next;
        }
        return root.next;
    }
}