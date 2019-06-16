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
// √ Accepted
//   √ 1563/1563 cases passed (120 ms)
//   √ Your runtime beats 28.34 % of csharp submissions
//   √ Your memory usage beats 55.74 % of csharp submissions (25.5 MB)
public class Solution {
    public ListNode AddTwoNumbers(ListNode l1, ListNode l2) {
        ListNode root=new ListNode(0);
        bool a =false;
        ListNode n =root;
        int r;
        while (l1 != null && l2!=null){
            if (a){
                r=l1.val+l2.val+1;
                a=false;
            }else{
                r=l1.val+l2.val;
            }
            if(r<10){
                n.next=new ListNode(r);
            }else{
                n.next=new ListNode(r%10);
                a=true;
            }
            l1=l1.next;
            l2=l2.next;
            n=n.next;
        }

        while (true){
            if(l1!=null){
                if(a){
                    r=l1.val+1;
                     a=false;
                }else{
                    r=l1.val;
                }
                if(r<10){
                     n.next=new ListNode(r);
               }else{
                    n.next=new ListNode(r%10);
                    a=true;
                }
                l1=l1.next;
                n=n.next;
                continue;
            }else if(l2!=null){
                if(a){
                    r=l2.val+1;
                     a=false;
                }else{
                    r=l2.val;
                }
                if(r<10){
                     n.next=new ListNode(r);
               }else{
                    n.next=new ListNode(r%10);
                    a=true;
                }
                l2=l2.next;
                n=n.next;
                continue;
            }else if(a){
                n.next = new ListNode(1);
                a=false;
            }
            break;
            }
        return root.next;
        }
    }


