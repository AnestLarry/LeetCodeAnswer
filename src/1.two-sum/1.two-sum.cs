/*
 * @lc app=leetcode id=1 lang=csharp
 *
 * [1] Two Sum
 Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

√ Accepted
  √ 29/29 cases passed (420 ms)
  √ Your runtime beats 29.04 % of csharp submissions
  √ Your memory usage beats 99.82 % of csharp submissions (28.4 MB)
 */
public class Solution {
    public int[] TwoSum(int[] nums, int target) {
        int l=nums.Length;
        for ( int i =0; i<l; i++){
            for (int j=i+1;j < l;j++){
                if (nums[i]+nums[j]==target){
                    return new int[] {i,j};
                }
            }
        }
        return new int[] {0,1};
    }
}

