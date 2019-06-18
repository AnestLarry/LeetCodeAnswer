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
//  √ Accepted
//   √ 16/16 cases passed (120 ms)
//   √ Your runtime beats 34.85 % of csharp submissions
//   √ Your memory usage beats 7.26 % of csharp submissions (29.7 MB)
public class Solution {
    public ListNode SortList(ListNode head) {
        List<int> lists = new List<int>();
        while (head != null){
            lists.Add(head.val);
            head=head.next;
        }
        lists.Sort();
        int l = lists.Count;
        ListNode root=new ListNode(0);
        ListNode n = root;
        for (int i =0 ;i<l;i++){
            n.next=new ListNode(lists[i]);
            n=n.next;
        }
        return root.next;
    }
}
