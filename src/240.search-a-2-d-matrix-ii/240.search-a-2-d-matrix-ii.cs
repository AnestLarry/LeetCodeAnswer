/*
 * @lc app=leetcode id=240 lang=csharp
 *
 * [240] Search a 2D Matrix II
 */
//  Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

// Integers in each row are sorted in ascending from left to right.
// Integers in each column are sorted in ascending from top to bottom.
// Example:

// Consider the following matrix:

// [
//   [1,   4,  7, 11, 15],
//   [2,   5,  8, 12, 19],
//   [3,   6,  9, 16, 22],
//   [10, 13, 14, 17, 24],
//   [18, 21, 23, 26, 30]
// ]
// Given target = 5, return true.

// Given target = 20, return false.
// Input data:
// [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]]
// 5

// Actual
//   × Compile Error
//   × runtime: N/A
//   × answer: 
//   × stdout: ''
//   × error: Line 10: Char 36: error CS0022: Wrong number of indices inside []; expected 2 (in Solution.cs)
//   × error: Line 10: Char 36: error CS0022: Wrong number of indices inside []; expected 2 (in Solution.cs)
// Line 13: Char 24: error CS0022: Wrong number of indices inside []; expected 2 (in Solution.cs)

// Expected
//   √ runtime: 4 ms
//   √ answer: true
//   √ stdout: ''
public class Solution {
    public bool SearchMatrix(int[,] matrix, int target) {
        if(matrix!=null){
            //Console.WriteLine(matrix[0]);
            int ml=matrix.Length,l=matrix[0].Length;
            for(int i =0 ;i<ml;i++){
                for(int j = 0; j<l;j++){
                    if(matrix[i][j]==target){
                        return true;
                    }
                }
            }
            return false;
        }
        return false;
    }
}

