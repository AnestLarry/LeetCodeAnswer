/*
 * @lc app=leetcode id=206 lang=golang
 *
 * [206] Reverse Linked List
 */
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//  Reverse a singly linked list.

// Example:

// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:

// A linked list can be reversed either iteratively or recursively. Could you implement both?
// √ Accepted
//   √ 27/27 cases passed (0 ms)
//   √ Your runtime beats 100 % of golang submissions
//   √ Your memory usage beats 34.64 % of golang submissions (2.6 MB)
func reverseList(head *ListNode) *ListNode {
    if head == nil || head.Next == nil{
		return head
	}
	pre,cur,temp := head,head.Next,head.Next.Next
	for cur!= nil{
		temp,cur.Next = cur.Next,pre
		pre,cur = cur,temp
	}
	head.Next=nil
	return pre
}

