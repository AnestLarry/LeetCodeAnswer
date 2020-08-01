/*
 * @lc app=leetcode.cn id=167 lang=java
 *
 * [167] Two Sum II - Input array is sorted
 */
//  Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

// The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

// Note:

// Your returned answers (both index1 and index2) are not zero-based.
// You may assume that each input would have exactly one solution and you may not use the same element twice.
// Example:

// Input: numbers = [2,7,11,15], target = 9
// Output: [1,2]
// Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
// @lc code=start
class Solution {
    public int[] twoSum(int[] numbers, int target) {
        // Accepted
        // 17/17 cases passed (1 ms)
        // Your runtime beats 96.98 % of java submissions
        // Your memory usage beats 6.67 % of java submissions (39.8 MB)
        int l = numbers.length;
        if (l < 3) {
            return new int[] { 1, 2 };
        }
        int i = 0, j = l - 1;
        while (i < j) {
            int r = numbers[i] + numbers[j];
            if (r == target) {
                return new int[] { i + 1, j + 1 };
            } else if (r > target) {
                j--;
            } else {
                i++;
            }
        }
        return new int[] { 1, 2 };
    }
}
// @lc code=end
