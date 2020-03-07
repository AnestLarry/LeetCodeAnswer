/*
 * @lc app=leetcode.cn id=118 lang=csharp
 *
 * [118] Pascal's Triangle
 */
// Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.

// In Pascal's triangle, each number is the sum of the two numbers directly above it.

// Example:

// Input: 5
// Output:
// [
//      [1],
//     [1,1],
//    [1,2,1],
//   [1,3,3,1],
//  [1,4,6,4,1]
// ]
// @lc code=start
public class Solution {
    public IList<IList<int>> Generate (int numRows) {
        // Accepted
        // 15/15 cases passed (236 ms)
        // Your runtime beats 94.74 % of csharp submissions
        // Your memory usage beats 6.82 % of csharp submissions (25.9 MB)
        if (numRows < 1) {
            return new int[][] { };
        }
        int[][] res = new int[numRows][];
        int i = 0;
        while (i < numRows) {
            res[i] = new int[i + 1];
            res[i][0] = res[i][i] = 1;
            int j = 1;
            while (j < i) {
                res[i][j] = res[i - 1][j - 1] + res[i - 1][j];
                j++;
            }
            i++;
        }
        return res;
    }
}
// @lc code=end