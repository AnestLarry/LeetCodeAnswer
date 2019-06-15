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
// √ Accepted
//   √ 208/208 cases passed (96 ms)
//   √ Your runtime beats 54.92 % of csharp submissions
//   √ Your memory usage beats 26.69 % of csharp submissions (23.8 MB)
public class Solution {
    public ListNode MergeTwoLists(ListNode l1, ListNode l2) {
        if(l1==null || l2==null){
            if (l1!=null){
                return l1;
            }else if (l2!=null){
                return l2;
            }else{
                return null;
            }
        }
        ListNode root = new ListNode(0);
        ListNode node = root;
        while(l1 != null && l2 != null){
            if (l1.val > l2.val){
                node.next = l2;
                l2 = l2.next;
            }else{
                node.next =l1;
                l1=l1.next;
            }
            node=node.next;
        }
        if (l1 != null){
            node.next =l1;
        }else{
            node.next =l2;
        }
        return root.next;
    }
}

