/*
 * @lc app=leetcode id=154 lang=csharp
 *
 * [154] Find Minimum in Rotated Sorted Array II
 */
//  Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

// Find the minimum element.

// The array may contain duplicates.

// Example 1:

// Input: [1,3,5]
// Output: 1
// Example 2:

// Input: [2,2,2,0,1]
// Output: 0
// Note:

// This is a follow up problem to Find Minimum in Rotated Sorted Array.
// Would allow duplicates affect the run-time complexity? How and why?
public class Solution {
    public int FindMin (int[] nums) {
        // Accepted
        // 192/192 cases passed (104 ms)
        // Your runtime beats 96.3 % of csharp submissions
        // Your memory usage beats 100 % of csharp submissions (25.1 MB)
        int l = nums.Length;
        if (l < 2) {
            return nums[0];
        }
        int last = l - 1, i = l - 2;
        while (i != -1 && nums[i] <= nums[last]) {
            if (nums[i >> 1] < nums[last]) {
                last = i >> 1;
                i = last - 1;
            } else {
                last = i;
                i--;
            }
        }
        return nums[last];
    }
}