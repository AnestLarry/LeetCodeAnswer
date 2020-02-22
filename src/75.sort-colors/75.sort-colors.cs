/*
 * @lc app=leetcode.cn id=75 lang=csharp
 *
 * [75] 颜色分类
 */
/*
Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?
*/
// @lc code=start
public class Solution {
    public void SortColors (int[] nums) {
        // Accepted
        // 87/87 cases passed (276 ms)
        // Your runtime beats 89.22 % of csharp submissions
        // Your memory usage beats 14.03 % of csharp submissions (29.2 MB)
        int left = 0, right = nums.Length - 1, cur = 0;
        while (cur <= right) {
            if (nums[cur] == 0) {
                if (nums[left] != nums[cur]) {
                    int temp = nums[cur];
                    nums[cur] = nums[left];
                    nums[left] = temp;
                }
                cur++;
                left++;
            } else if (nums[cur] == 2) {
                if (nums[cur] != nums[right]) {
                    int temp = nums[cur];
                    nums[cur] = nums[right];
                    nums[right] = temp;
                }
                right--;
            } else {
                ++cur;
            }
        }
    }
}
// @lc code=end