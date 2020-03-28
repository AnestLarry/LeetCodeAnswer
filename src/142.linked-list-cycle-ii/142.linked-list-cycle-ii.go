/*
 * @lc app=leetcode.cn id=142 lang=golang
 *
 * [142] Linked List Cycle II
 */
//  Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

// To represent a cycle in the given linked list, we use an integer pos which represents the position (0-indexed) in the linked list where tail connects to. If pos is -1, then there is no cycle in the linked list.

// Note: Do not modify the linked list.

// Example 1:

// Input: head = [3,2,0,-4], pos = 1
// Output: tail connects to node index 1
// Explanation: There is a cycle in the linked list, where tail connects to the second node.

// @lc code=start
/**
 * Definition for singly-linked list.
 * type ListNode struct {
 *     Val int
 *     Next *ListNode
 * }
 */
func detectCycle(head *ListNode) *ListNode {
	// Accepted
	// 16/16 cases passed (8 ms)
	// Your runtime beats 85.38 % of golang submissions
	// Your memory usage beats 74.44 % of golang submissions (3.8 MB)
	if head == nil || head.Next == nil {
		return nil
	}
	slow, fast := head, head
	for fast != nil && fast.Next != nil {
		slow = slow.Next
		fast = fast.Next.Next
		if slow == fast {
			break
		}
	}
	if fast == nil || fast.Next == nil {
		return nil
	}

	for head != fast {
		head = head.Next
		fast = fast.Next
	}
	return fast
}

// @lc code=end
