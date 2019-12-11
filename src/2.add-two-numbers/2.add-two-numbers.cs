/*
 * @lc app=leetcode id=2 lang=csharp
 *
 * [2] Add Two Numbers
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
 */
//  You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.
public class Solution
{
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2)
    {
        // Accepted
        // 1563/1563 cases passed (132 ms)
        // Your runtime beats 70.08 % of csharp submissions
        // Your memory usage beats 5.07 % of csharp submissions (26.8 MB)
        ListNode root = new ListNode(0), n = root;
        bool flag = false;
        while (l1 != null || l2 != null || flag)
        {
            int v1 = 0, v2 = 0, val;
            if (l1 != null)
            {
                v1 = l1.val;
                l1 = l1.next;
            }
            if (l2 != null)
            {
                v2 = l2.val;
                l2 = l2.next;
            }
            val = flag ? v1 + v2 + 1 : v1 + v2;
            flag = false;
            if (val < 10)
            {
                n.next = new ListNode(val);
            }
            else
            {
                n.next = new ListNode(val - 10);
                flag = true;
            }
            n = n.next;
        }
        return root.next;
    }
}


