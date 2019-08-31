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

public class Solution
{
    public void MoveZeroes(int[] nums)
    {
        // √ Accepted
        //   √ 21/21 cases passed (256 ms)
        //   √ Your runtime beats 91.83 % of csharp submissions
        //   √ Your memory usage beats 50 % of csharp submissions (30 MB)
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
    public void MoveZeroes2(int[] nums)
    {
        // √ Accepted
        //     √ 21/21 cases passed (244 ms)
        //     √ Your runtime beats 99.73 % of csharp submissions
        //     √ Your memory usage beats 75 % of csharp submissions (30 MB)
        int i = 0, l = nums.Length, n = 0;
        if (l > 1)
        {
            while (i < l)
            {
                if (nums[i] != 0)
                {
                    if (i != n)
                    {
                        nums[n] ^= nums[i];
                        nums[i] ^= nums[n];
                        nums[n] ^= nums[i];
                    }

                    n += 1;
                }
                i++;
            }
        }
    }
}
