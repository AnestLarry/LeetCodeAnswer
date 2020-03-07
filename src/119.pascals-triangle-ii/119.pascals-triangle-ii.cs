/*
 * @lc app=leetcode.cn id=119 lang=csharp
 *
 * [119] Pascal's Triangle II
 */
// Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.

// Note that the row index starts from 0.


// In Pascal's triangle, each number is the sum of the two numbers directly above it.

// Example:

// Input: 3
// Output: [1,3,3,1]
// Follow up:

// Could you optimize your algorithm to use only O(k) extra space?
// @lc code=start
public class Solution {
    public IList<int> GetRow (int rowIndex) {
        // Accepted
        // 34/34 cases passed (236 ms)
        // Your runtime beats 87.76 % of csharp submissions
        // Your memory usage beats 6.67 % of csharp submissions (25.5 MB)
        int[] res = new int[rowIndex + 1];
        for (int i = 0; i <= rowIndex; i++) {
            res[i] = 1;
            for (int j = i; j > 1; j--) {
                res[j - 1] = res[j - 1] + res[j - 2];
            }
        }
        return res;
    }
}
// @lc code=end