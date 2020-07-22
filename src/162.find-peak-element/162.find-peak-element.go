/*
 * @lc app=leetcode.cn id=162 lang=golang
 *
 * [162] Find Peak Element
 */
/*
A peak element is an element that is greater than its neighbors.

Given an input array nums, where nums[i] ≠ nums[i+1], find a peak element and return its index.

The array may contain multiple peaks, in that case return the index to any one of the peaks is fine.

You may imagine that nums[-1] = nums[n] = -∞.

Example 1:

Input: nums = [1,2,3,1]
Output: 2
Explanation: 3 is a peak element and your function should return the index number 2.
Example 2:

Input: nums = [1,2,1,3,5,6,4]
Output: 1 or 5
Explanation: Your function can return either index number 1 where the peak element is 2,
             or index number 5 where the peak element is 6.
Note:

Your solution should be in logarithmic complexity.

*/
// @lc code=start
func findPeakElement(nums []int) int {
	// Accepted
	// 59/59 cases passed (4 ms)
	// Your runtime beats 85.04 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (2.8 MB)
	h, i, t, l := 0, 0, len(nums), len(nums)
	for l > 1 {
		if l < 3 {
			if nums[h] > nums[h+1] {
				i = h
			} else {
				i = h + 1
			}
			l = 1
		} else {
			m := (t + h) >> 1
			if nums[m] > nums[m-1] {
				h = m
			} else {
				t = m + 1
			}
			l = t - h
		}
	}
	return i
}

// @lc code=end
