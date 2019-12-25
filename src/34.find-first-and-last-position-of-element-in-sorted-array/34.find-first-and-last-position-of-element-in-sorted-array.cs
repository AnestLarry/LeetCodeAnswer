/*
 * @lc app=leetcode.cn id=34 lang=csharp
 *
 * [34] Find First and Last Position of Element in Sorted Array
 */
// Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

// Your algorithm's runtime complexity must be in the order of O(log n).

// If the target is not found in the array, return [-1, -1].

// Example 1:

// Input: nums = [5,7,7,8,8,10], target = 8
// Output: [3,4]
// Example 2:

// Input: nums = [5,7,7,8,8,10], target = 6
// Output: [-1,-1]
// @lc code=start
public class Solution
{
    public int[] SearchRange(int[] nums, int target)
    {
        // Accepted
        // 88/88 cases passed (288 ms)
        // Your runtime beats 91.92 % of csharp submissions
        // Your memory usage beats 8 % of csharp submissions (31.1 MB)
        int first = -1, last = -1, len = nums.Length;
        if (len < 1)
        {
            return new int[] { -1, -1 };
        }
        for (int i = 0; i < len; i++)
        {
            if (nums[i] < target)
            {
                continue;
            }
            else if (nums[i] == target)
            {
                first = last = i;
                for (int j = i; j < len; j++)
                {
                    if (nums[j] == nums[i])
                    {
                        last = j;
                    }
                    else
                    {
                        return new int[] { first, last };
                    }
                }
            }
            break;
        }
        return new int[] { first, last };
    }
}
// @lc code=end

