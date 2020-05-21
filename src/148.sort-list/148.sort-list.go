/*
 * @lc app=leetcode id=148 lang=golang
 *
 * [148] Sort List
 */
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
//  Sort a linked list in O(n log n) time using constant space complexity.

// Example 1:

// Input: 4->2->1->3
// Output: 1->2->3->4
// Example 2:

// Input: -1->5->3->4->0
// Output: -1->0->3->4->5
import "sort"

func sortList(head *ListNode) *ListNode {
	// Accepted
	// 16/16 cases passed (12 ms)
	// Your runtime beats 91.43 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (5.1 MB)
	if head == nil || head.Next == nil {
		return head
	}
	slow, fast := head, head
	for fast.Next != nil && fast.Next.Next != nil {
		slow, fast = slow.Next, fast.Next.Next
	}
	leftTail := slow
	slow = slow.Next
	leftTail.Next = nil
	left, right := sortList(head), sortList(slow)
	return mergeLinked(left, right)
}

func mergeLinked(left *ListNode, right *ListNode) *ListNode {
	cur := &ListNode{}
	temp := cur
	for left != nil && right != nil {
		if left.Val < right.Val {
			cur.Next = left
			left = left.Next
		} else {
			cur.Next = right
			right = right.Next
		}
		cur = cur.Next
	}
	if left != nil {
		cur.Next = left
	} else if right != nil {
		cur.Next = right
	}
	return temp.Next
}

func sortList2(head *ListNode) *ListNode {
	// √ Accepted
	//   √ 16/16 cases passed (12 ms)
	//   √ Your runtime beats 90.75 % of golang submissions
	//   √ Your memory usage beats 18.6 % of golang submissions (6.7 MB)
	lists := []int{}
	for head != nil {
		lists = append(lists, head.Val)
		head = head.Next
	}
	sort.Ints(lists)
	root := &ListNode{Val: 1}
	n, l := root, len(lists)
	for i := 0; i < l; i++ {
		n.Next = &ListNode{Val: lists[i]}
		n = n.Next
	}
	return root.Next
}
