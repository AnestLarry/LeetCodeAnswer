/*
 * @lc app=leetcode id=283 lang=csharp
 *
 * [283] Move Zeroes
 */
//  Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

// Example:

// Input: [0,1,0,3,12]
// Output: [1,3,12,0,0]
// Note:

// You must do this in-place without making a copy of the array.
// Minimize the total number of operations.
//  √ Accepted
//   √ 21/21 cases passed (260 ms)
//   √ Your runtime beats 82.01 % of csharp submissions
//   √ Your memory usage beats 56.25 % of csharp submissions (30 MB)
public class Solution
{
    public void MoveZeroes(int[] nums)
    {
        int i = 0, l = nums.Length, n = 0;
        if (l > 1)
        {
            while (i < l)
            {
                if (nums[i] != 0)
                {
                    int temp = nums[n];
                    nums[n] = nums[i];
                    nums[i] = temp;
                    n += 1;
                }
                i++;
            }
        }
    }
}
