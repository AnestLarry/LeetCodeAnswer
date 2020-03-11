/*
 * @lc app=leetcode.cn id=136 lang=csharp
 *
 * [136] Single Number
 */
/*
Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4
*/
// @lc code=start
public class Solution {
    public int SingleNumber (int[] nums) {
        // Accepted
        // 16/16 cases passed (112 ms)
        // Your runtime beats 97.19 % of csharp submissions
        // Your memory usage beats 72.73 % of csharp submissions (25.6 MB)
        int r = 0;
        foreach (int i in nums) {
            r ^= i;
        }
        return r;
    }
}
// @lc code=end