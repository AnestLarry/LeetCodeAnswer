/*
 * @lc app=leetcode id=206 lang=cpp
 *
 * [206] Reverse Linked List
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
// Reverse a singly linked list.

// Example:

// Input: 1->2->3->4->5->NULL
// Output: 5->4->3->2->1->NULL
// Follow up:

// A linked list can be reversed either iteratively or recursively. Could you implement both?
class Solution
{
public:
    ListNode *reverseList(ListNode *head)
    {
        // Accepted
        // 27/27 cases passed (4 ms)
        // Your runtime beats 98.92 % of cpp submissions
        // Your memory usage beats 100 % of cpp submissions (9.1 MB)
        if (head == NULL || head->next == NULL)
        {
            return head;
        }
        ListNode *prev = head;
        ListNode *cur = head->next;
        while(cur !=NULL){
            ListNode* temp = cur->next;
            cur->next = prev;
            prev = cur;
            cur = temp;
        }
        head->next = NULL;
        return prev;
    }
};
// @lc code=end
