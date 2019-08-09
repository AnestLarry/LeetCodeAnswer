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
//  √ Accepted
//   √ 275/275 cases passed (100 ms)
//   √ Your runtime beats 73.16 % of csharp submissions
//   √ Your memory usage beats 50 % of csharp submissions (23.3 MB)
public class Solution {
    public bool Search(int[] nums, int target) {
        int l=nums.Length;
        if(l<1){
            return false;
        }
        if(target>=nums[0]){
            int last=0,i=0;
            while(i<l && nums[i]>=nums[last]){
                if (nums[i] == target)
                {
                    return true;
                }
                last=i;
                i++;
            }
            return false;
        }else{
            int last=l-1,i=l-1;
            while(i>0 && nums[i]<=nums[last]){
                if(nums[i]==target){
                    return true;
                }
                last=i;
                i--;
            }
            return false;
        }
    }
}
