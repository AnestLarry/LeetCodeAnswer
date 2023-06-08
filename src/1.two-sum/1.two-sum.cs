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
 */
public class Solution {
    public int[] TwoSum (int[] nums, int target) {
        // Accepted
        // 29/29 cases passed (280 ms)
        // Your runtime beats 95.59 % of csharp submissions
        // Your memory usage beats 33.77 % of csharp submissions (31 MB)
        Dictionary<int, int> m = new Dictionary<int, int> ();
        for (int i = 0; i < nums.Length; i++) {
            if (m.ContainsKey (target - nums[i])) {
                return new int[] { m[target - nums[i]], i };
            } else {
                m[nums[i]] = i;
            }
        }
        return new int[] {-1, -1 };
    }
}