/*
 * @lc app=leetcode id=74 lang=csharp
 *
 * [74] Search a 2D Matrix
 */
//  Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

// Integers in each row are sorted from left to right.
// The first integer of each row is greater than the last integer of the previous row.
// Example 1:

// Input:
// matrix = [
//   [1,   3,  5,  7],
//   [10, 11, 16, 20],
//   [23, 30, 34, 50]
// ]
// target = 3
// Output: true
// Example 2:

// Input:
// matrix = [
//   [1,   3,  5,  7],
//   [10, 11, 16, 20],
//   [23, 30, 34, 50]
// ]
// target = 13
// Output: false
//  √ Accepted
//   √ 136/136 cases passed (92 ms)
//   √ Your runtime beats 99.51 % of csharp submissions
//   √ Your memory usage beats 100 % of csharp submissions (23.9 MB)
public class Solution {
    public bool SearchMatrix(int[][] matrix, int target) {
        int l=matrix.Length;
        if(l<1){
            return false;
        }
        int ll = matrix[0].Length;
        if (ll<1){
            return false;
        }
        for(int i =0;i<l;i++){
            if (matrix[i][ll-1] >= target)
            {
                for (int j = 0; j < ll; j++)
                {
                    if (matrix[i][j] == target)
                    {
                        return true;
                    }
                }
                return false;
            }
            else
            {
                continue;
            }
        }
        return false;
    }
}
