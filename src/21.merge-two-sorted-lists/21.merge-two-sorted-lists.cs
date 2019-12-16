/*
 * @lc app=leetcode id=21 lang=csharp
 *
 * [21] Merge Two Sorted Lists
 */
/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     public int val;
 *     public ListNode next;
 *     public ListNode(int x) { val = x; }
 * }
*/
//  Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

// Example:

// Input: 1->2->4, 1->3->4
// Output: 1->1->2->3->4->4
public class Solution
{
    public ListNode MergeTwoLists(ListNode l1, ListNode l2)
    {
        // Accepted
        // 208/208 cases passed (108 ms)
        // Your runtime beats 88.15 % of csharp submissions
        // Your memory usage beats 5.36 % of csharp submissions (25 MB)
        if (l1 == null || l2 == null)
        {
            return l1 != null ? l1 : l2;
        }
        if (l1.val <= l2.val)
        {
            l1.next = MergeTwoLists(l1.next, l2);
            return l1;
        }
        else
        {
            l2.next = MergeTwoLists(l1, l2.next);
            return l2;
        }
    }
    public ListNode MergeTwoLists2(ListNode l1, ListNode l2)
    {
        // Accepted
        // 208/208 cases passed (112 ms)
        // Your runtime beats 75.8 % of csharp submissions
        // Your memory usage beats 5.36 % of csharp submissions (24.9 MB)
        if (l1 == null || l2 == null)
        {
            return l1 != null ? l1 : l2;
        }
        ListNode root = new ListNode(0);
        ListNode node = root;
        while (l1 != null && l2 != null)
        {
            if (l1.val > l2.val)
            {
                node.next = l2;
                l2 = l2.next;
            }
            else
            {
                node.next = l1;
                l1 = l1.next;
            }
            node = node.next;
        }
        node.next = l1 != null ? l1 : l2;
        return root.next;
    }
}

