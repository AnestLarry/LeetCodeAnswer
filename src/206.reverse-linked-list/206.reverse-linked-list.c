/*
 * @lc app=leetcode id=206 lang=c
 *
 * [206] Reverse Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
// Reverse a singly linked list.

// Example:

// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:

// A linked list can be reversed either iteratively or recursively. Could you implement both?

struct ListNode *reverseList(struct ListNode *head)
{
    // Accepted
    // 27/27 cases passed (4 ms)
    // Your runtime beats 73.41 % of c submissions
    // Your memory usage beats 54.17 % of c submissions (7.7 MB)
    if (head == NULL || head->next == NULL)
    {
        return head;
    }
    struct ListNode *root = head;
    struct ListNode *prev = head;
    struct ListNode *cur = head->next;
    while (cur != NULL)
    {
        struct ListNode *temp = cur->next;
        cur->next = prev;
        prev = cur;
        cur = temp;
    }
    root->next = NULL;
    return prev;
}

// @lc code=end
