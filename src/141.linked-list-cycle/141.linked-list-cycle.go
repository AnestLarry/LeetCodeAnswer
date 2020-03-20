/*
 * @lc app=leetcode.cn id=141 lang=golang
 *
 * [141] Linked List Cycle
 */
//  Given a linked list, determine if it has a cycle in it.

// To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

// Example 1:

// Input: head = [3,2,0,-4], pos = 1
// Output: true
// Explanation: There is a cycle in the linked list, where tail connects to the second node.

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func hasCycle(head *ListNode) bool {
	// Accepted
	// 17/17 cases passed (8 ms)
	// Your runtime beats 82.03 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (3.8 MB)
	if head == nil || head.Next == nil {
		return false
	}
	root := head.Next
	for root.Next != nil {
		if root.Next == head {
			return true
		}
		root.Next, root = head, root.Next
	}
	return false
}

// @lc code=end
