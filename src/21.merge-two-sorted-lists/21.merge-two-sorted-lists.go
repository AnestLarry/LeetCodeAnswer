/*
 * @lc app=leetcode id=21 lang=golang
 *
 * [21] Merge Two Sorted Lists
 */
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//  Merge two sorted linked lists and return it as a new list. The new list should be made by splicing together the nodes of the first two lists.

// Example:

// Input: 1->2->4, 1->3->4
// Output: 1->1->2->3->4->4
//  √ Accepted
//  √ 208/208 cases passed (0 ms)
//  √ Your runtime beats 100 % of golang submissions
//  √ Your memory usage beats 100 % of golang submissions (2.5 MB)
func mergeTwoLists(l1 *ListNode, l2 *ListNode) *ListNode {
	if l1 == nil || l2 == nil {
		if l1 != nil {
			return l1
		} else if l2 != nil {
			return l2
		}
		return nil
	}
	root := new(ListNode)
	n := root
	for l1 != nil && l2 != nil {
		if l1.Val > l2.Val {
			n.Next = l2
			l2 = l2.Next
		} else {
			n.Next = l1
			l1 = l1.Next
		}
		n = n.Next
	}
	if l1 != nil {
		n.Next = l1
	} else {
		n.Next = l2
	}
	return root.Next
}
