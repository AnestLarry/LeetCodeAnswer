/*
 * @lc app=leetcode id=206 lang=csharp
 *
 * [206] Reverse Linked List
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
//  Reverse a singly linked list.

// Example:

// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:

// A linked list can be reversed either iteratively or recursively. Could you implement both?
// √ Accepted
//   √ 27/27 cases passed (92 ms)
//   √ Your runtime beats 94.67 % of csharp submissions
//   √ Your memory usage beats 56.96 % of csharp submissions (22.4 MB)
public class Solution {
    public ListNode ReverseList(ListNode head) {
        if(head == null||head.next == null){
            return head;
        }
        ListNode pre = head,cur = head.next,temp = head.next.next;

        while(cur != null){
            temp = cur.next;
            cur.next = pre;
            pre = cur;
            cur = temp;
        }
        head.next = null;
        return pre;

    }
}
