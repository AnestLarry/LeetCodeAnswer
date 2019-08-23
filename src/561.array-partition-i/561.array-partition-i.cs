/*
 * @lc app=leetcode id=561 lang=csharp
 *
 * [561] Array Partition I
 */
//  Given an array of 2n integers, your task is to group these integers into n pairs of integer, say (a1, b1), (a2, b2), ..., (an, bn) which makes sum of min(ai, bi) for all i from 1 to n as large as possible.

// Example 1:
// Input: [1,4,3,2]

// Output: 4
// Explanation: n is 2, and the maximum sum of pairs is 4 = min(1, 2) + min(3, 4).
// Note:
// 1. n is a positive integer, which is in the range of [1, 10000].
// 2. All the integers in the array will be in the range of [-10000, 10000].
// √ Accepted
//   √ 81/81 cases passed (184 ms)
//   √ Your runtime beats 27.44 % of csharp submissions
//   √ Your memory usage beats 11.11 % of csharp submissions (33.1 MB)
public class Solution {
    public int ArrayPairSum(int[] nums) {
        Array.Sort(nums);
        int sum=0,l=nums.Length;
        foreach(int i in Enumerable.Range(0, (int)l/2).Select(x => x*2) ){
            sum+=nums[i];
        }
        return sum;
    }
}

