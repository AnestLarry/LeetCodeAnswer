/*
 * @lc app=leetcode id=35 lang=csharp
 *
 * [35] Search Insert Position
 */
//  Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

// You may assume no duplicates in the array.

// Example 1:

// Input: [1,3,5,6], 5
// Output: 2
// Example 2:

// Input: [1,3,5,6], 2
// Output: 1
// Example 3:

// Input: [1,3,5,6], 7
// Output: 4
// Example 4:

// Input: [1,3,5,6], 0
// Output: 0

public class Solution
{
    public int SearchInsert(int[] nums, int target)
    {
        // Accepted
        // 62/62 cases passed (108 ms)
        // Your runtime beats 89.6 % of csharp submissions
        // Your memory usage beats 5.71 % of csharp submissions (24.1 MB)
        int i = 0, l = nums.Length;
        while (i < l)
        {
            if (nums[i] >= target)
            {
                return i;
            }
            i++;
        }
        return l;
    }
    public int SearchInsert2(int[] nums, int target)
    {
        // Accepted
        // 62/62 cases passed (100 ms)
        // Your runtime beats 99.08 % of csharp submissions
        // Your memory usage beats 5.71 % of csharp submissions (23.9 MB)
        int left = 0, right = nums.Length - 1, mid;
        while (left <= right)
        {
            mid = (left + right) >> 1;
            if (nums[mid] == target)
            {
                return mid;
            }
            if (nums[mid] < target)
            {
                left = mid + 1;
            }
            else
            {
                right = mid - 1;
            }
        }
        return left;

    }
}

