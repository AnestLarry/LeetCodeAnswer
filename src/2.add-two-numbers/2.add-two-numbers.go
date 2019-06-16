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
//  √ Accepted
//   √ 1563/1563 cases passed (12 ms)
//   √ Your runtime beats 86.23 % of golang submissions
//   √ Your memory usage beats 66.33 % of golang submissions (5 MB)
func addTwoNumbers(l1 *ListNode, l2 *ListNode) *ListNode {
	root := new(ListNode)
	n, a, r := root, false, 0
	for l1 != nil && l2 != nil {
		if a {
			r = l1.Val + l2.Val + 1
			a = false
		} else {
			r = l1.Val + l2.Val
		}
		if r < 10 {
			n.Next = &ListNode{Val: r}
		} else {
			n.Next = &ListNode{Val: r % 10}
			a = true
		}
		l1, l2, n = l1.Next, l2.Next, n.Next
	}

	for true {
		if l1 != nil {
			if a {
				r = l1.Val + 1
				a = false
			} else {
				r = l1.Val
			}
			if r < 10 {
				n.Next = &ListNode{Val: r}
			} else {
				n.Next = &ListNode{Val: r % 10}
				a = true
			}
			l1, n = l1.Next, n.Next
			continue
		} else if l2 != nil {
			if a {
				r = l2.Val + 1
				a = false
			} else {
				r = l2.Val
			}
			if r < 10 {
				n.Next = &ListNode{Val: r}
			} else {
				n.Next = &ListNode{Val: r % 10}
				a = true
			}
			l2, n = l2.Next, n.Next
			continue
		} else if a {
			n.Next = &ListNode{Val: 1}
			a = false

		}
		break
	}
	return root.Next
}