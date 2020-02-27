/*
 * @lc app=leetcode id=81 lang=csharp
 *
 * [81] Search in Rotated Sorted Array II
 */
//  Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

// You are given a target value to search. If found in the array return true, otherwise return false.

// Example 1:

// Input: nums = [2,5,6,0,0,1,2], target = 0
// Output: true
// Example 2:

// Input: nums = [2,5,6,0,0,1,2], target = 3
// Output: false
// Follow up:

// This is a follow up problem to Search in Rotated Sorted Array, where nums may contain duplicates.
// Would this affect the run-time complexity? How and why?
public class Solution {
    public bool Search (int[] nums, int target) {
        // Accepted
        // 275/275 cases passed (108 ms)
        // Your runtime beats 89.19 % of csharp submissions
        // Your memory usage beats 20 % of csharp submissions (25.4 MB)        int l = 0, r = nums.Length - 1;
        int l = 0, r = nums.Length - 1;
        if (r < 0) {
            return false;
        }
        while (l <= r) {
            int mid = l + ((r - l) >> 1);
            if (nums[mid] == target) return true;
            while (l < mid && nums[l] == nums[mid]) l++;
            if (nums[l] <= nums[mid]) {
                if (nums[l] <= target && target < nums[mid]) {
                    r = --mid;
                } else {
                    l = ++mid;
                }
            } else {
                if (nums[mid] < target && target <= nums[r]) {
                    l = ++mid;
                } else {
                    r = --mid;
                }
            }
        }
        return false;
    }

    public bool Search2 (int[] nums, int target) {
        // Accepted
        // 275/275 cases passed (112 ms)
        // Your runtime beats 64.86 % of csharp submissions
        // Your memory usage beats 20 % of csharp submissions (25.3 MB)
        int l = nums.Length;
        if (l < 1) {
            return false;
        }
        if (target >= nums[0]) {
            int last = 0, i = 0;
            while (i < l && nums[i] >= nums[last]) {
                if (nums[i] == target) {
                    return true;
                }
                last = i;
                i++;
            }
            return false;
        } else {
            int last = l - 1, i = l - 1;
            while (i > 0 && nums[i] <= nums[last]) {
                if (nums[i] == target) {
                    return true;
                }
                last = i;
                i--;
            }
            return false;
        }
    }
}