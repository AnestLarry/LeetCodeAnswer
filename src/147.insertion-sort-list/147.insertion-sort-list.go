/*
 * @lc app=leetcode.cn id=147 lang=golang
 *
 * [147] Insertion Sort List
 */
// A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
// With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

// Algorithm of Insertion Sort:

// Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
// At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
// It repeats until no input elements remain.

// Example 1:

// Input: 4->2->1->3
// Output: 1->2->3->4
// Example 2:

// Input: -1->5->3->4->0
// Output: -1->0->3->4->5

// @lc code=start
// Definition for singly-linked list.
// type ListNode struct {
// 	Val  int
// 	Next *ListNode
// }

func insertionSortList(head *ListNode) *ListNode {
	// Accepted
	// 22/22 cases passed (4 ms)
	// Your runtime beats 98.8 % of golang submissions
	// Your memory usage beats 69.09 % of golang submissions (3.3 MB)
	if head == nil || head.Next == nil {
		return head
	}
	h, cur := &ListNode{-1, head}, head
	pre := h
	for cur != nil {
		lat := cur.Next
		if lat != nil && lat.Val < cur.Val {
			for pre.Next != nil && pre.Next.Val < lat.Val {
				pre = pre.Next
			}
			pre.Next, cur.Next, lat.Next, pre = lat, lat.Next, pre.Next, h
		} else {
			cur = lat
		}
	}
	return h.Next
}

// @lc code=end
