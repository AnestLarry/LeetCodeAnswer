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
// √ Accepted
//   √ 16/16 cases passed (12 ms)
//   √ Your runtime beats 90.75 % of golang submissions
//   √ Your memory usage beats 18.6 % of golang submissions (6.7 MB)
import "sort"

func sortList(head *ListNode) *ListNode {
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
