/*
 * @lc app=leetcode.cn id=147 lang=csharp
 *
 * [147] Insertion Sort List
 */
// A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
// With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list


// Algorithm of Insertion Sort:

// Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
// At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
// It repeats until no input elements remain.

// Example 1:

// Input: 4->2->1->3
// Output: 1->2->3->4
// Example 2:

// Input: -1->5->3->4->0
// Output: -1->0->3->4->5
// @lc code=start

//Definition for singly-linked list.
// public class ListNode {
//     public int val;
//     public ListNode next;
//     public ListNode (int x) { val = x; }
// }

public class Solution {
    public ListNode InsertionSortList (ListNode head) {
        // Accepted
        // 22/22 cases passed (112 ms)
        // Your runtime beats 95.45 % of csharp submissions
        // Your memory usage beats 14.29 % of csharp submissions (25.2 MB)
        if (head == null || head.next == null) {
            return head;
        }
        ListNode h = new ListNode (-1), cur = head, pre = h;
        h.next = head;
        while (cur != null) {
            ListNode lat = cur.next;
            if (lat != null && lat.val < cur.val) {
                while (pre.next != null && pre.next.val < lat.val) {
                    pre = pre.next;
                }
                ListNode tmp = pre.next;
                pre.next = lat;
                cur.next = lat.next;
                lat.next = tmp;
                pre = h;
            } else {
                cur = lat;
            }
        }
        return h.next;
    }
    public ListNode InsertionSortList2 (ListNode head) {
        // Accepted
        // 22/22 cases passed (144 ms)
        // Your runtime beats 54.55 % of csharp submissions
        // Your memory usage beats 7.14 % of csharp submissions (25.4 MB)
        if (head == null || head.next == null) {
            return head;
        }
        ListNode h = new ListNode (-1), cur = head, lat = cur.next;
        h.next = head;
        while (lat != null) {
            ListNode tmp = h.next, pre = h;
            while (tmp != null && tmp.val < lat.val) {
                tmp = tmp.next;
                pre = pre.next;
            }
            if (tmp == lat) {
                cur = lat;
            } else {
                cur.next = lat.next;
                lat.next = tmp;
                pre.next = lat;
            }
            lat = cur.next;
        }
        return h.next;
    }
}
// @lc code=end