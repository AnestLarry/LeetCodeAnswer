/*
 * @lc app=leetcode id=53 lang=golang
 *
 * [53] Maximum Subarray
 */
/*Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Follow up:

If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.*/
// @lc code=start
func maxSubArray(nums []int) int {
	// Accepted
	// 202/202 cases passed (4 ms)
	// Your runtime beats 97.21 % of golang submissions
	// Your memory usage beats 57.14 % of golang submissions (3.3 MB)
	nums_len := len(nums)
	if nums_len == 1 {
		return nums[0]
	}
	bl := nums[0]
	maxnum := nums[0]
	for i := 1; i < nums_len; i += 1 {
		if bl > 0 {
			bl = bl + nums[i]
		} else {
			bl = nums[i]
		}
		if bl > maxnum {
			maxnum = bl
		}
	}
	return maxnum
}

// @lc code=end