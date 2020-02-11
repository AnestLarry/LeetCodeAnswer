/*
 * @lc app=leetcode id=73 lang=csharp
 *
 * [73] Set Matrix Zeroes
 */
//  Given a m x n matrix, if an element is 0, set its entire row and column to 0. Do it in-place.

// Example 1:

// Input: 
// [
//   [1,1,1],
//   [1,0,1],
//   [1,1,1]
// ]
// Output: 
// [
//   [1,0,1],
//   [0,0,0],
//   [1,0,1]
// ]
// Example 2:

// Input: 
// [
//   [0,1,2,0],
//   [3,4,5,2],
//   [1,3,1,5]
// ]
// Output: 
// [
//   [0,0,0,0],
//   [0,4,5,0],
//   [0,3,1,0]
// ]
// Follow up:

// A straight forward solution using O(mn) space is probably a bad idea.
// A simple improvement uses O(m + n) space, but still not the best solution.
// Could you devise a constant space solution?
// √ Accepted
//   √ 159/159 cases passed (308 ms)
//   √ Your runtime beats 14.83 % of csharp submissions
//   √ Your memory usage beats 22.3 % of csharp submissions (31.8 MB)
public class Solution {
    // Accepted
    // 159/159 cases passed (312 ms)
    // Your runtime beats 100 % of csharp submissions
    // Your memory usage beats 66.67 % of csharp submissions (32.5 MB)
    public void SetZeroes (int[][] matrix) {
        int ml = matrix.Length, l = matrix[0].Length;
        List<List<int>> z = new List<List<int>> ();
        for (int i = 0; i < ml; i++) {
            for (int j = 0; j < l; j++) {
                if (matrix[i][j] == 0) {
                    z.Add (new List<int> (new int[] { i, j }));
                }
            }
        }
        // Readable Code
        //
        // Accepted
        // 159/159 cases passed (316 ms)
        // Your runtime beats 95.24 % of csharp submissions
        // Your memory usage beats 46.67 % of csharp submissions (32.6 MB)
        //
        // if (z != null) {
        //     for (int i = 0; i < z.Count (); i++) {
        //         for (int j = 0; j < l; j++) {
        //             matrix[z[i][0]][j] = 0;
        //         }
        //         for (int j = 0; j < ml; j++) {
        //             matrix[j][z[i][1]] = 0;
        //         }
        //     }
        // }
        if (z != null) {
            if (l > ml) {
                for (int i = 0; i < z.Count (); i++) {
                    int j = 0;

                    for (; j < ml; j++) {
                        matrix[z[i][0]][j] = 0;
                        matrix[j][z[i][1]] = 0;
                    }
                    for (; j < l; j++) {
                        matrix[z[i][0]][j] = 0;
                    }
                }
            } else {
                for (int i = 0; i < z.Count (); i++) {
                    int j = 0;

                    for (; j < l; j++) {
                        matrix[z[i][0]][j] = 0;
                        matrix[j][z[i][1]] = 0;
                    }
                    for (; j < ml; j++) {
                        matrix[j][z[i][1]] = 0;
                    }
                }
            }
        }
    }
}