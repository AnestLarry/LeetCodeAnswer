/*
 * @lc app=leetcode id=2 lang=golang
 *
 * [2] Add Two Numbers
 */
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//  You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.

// You may assume the two numbers do not contain any leading zero, except the number 0 itself.

// Example:

// Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
// Output: 7 -> 0 -> 8
// Explanation: 342 + 465 = 807.
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	// Accepted
	// 1563/1563 cases passed (12 ms)
	// Your runtime beats 81.21 % of golang submissions
	// Your memory usage beats 72.11 % of golang submissions (5 MB)
	root := &ListNode{Val: 0}
	n, flag := root, false
	for l1 != nil || l2 != nil || flag {
		v1, v2, val := 0, 0, 0
		if l1 != nil {
			v1 = l1.Val
			l1 = l1.Next
		}
		if l2 != nil {
			v2 = l2.Val
			l2 = l2.Next
		}
		if flag {
			val = v1 + v2 + 1
			flag = false
		} else {
			val = v1 + v2
		}
		if val < 10 {
			n.Next = &ListNode{Val: val}
		} else {
			n.Next = &ListNode{Val: val - 10}
			flag = true
		}
		n = n.Next
	}
	return root.Next
}