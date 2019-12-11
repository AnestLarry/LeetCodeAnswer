/*
 * @lc app=leetcode id=1 lang=golang
 *
 * [1] Two Sum
 Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
*/

func twoSum(nums []int, target int) []int {
	// Accepted
	// 29/29 cases passed (4 ms)
	// Your runtime beats 96.89 % of golang submissions
	// Your memory usage beats 29.3 % of golang submissions (3.8 MB)
	m := make(map[int]int)
	for i := 0; i < len(nums); i++ {
		_, ok := m[nums[i]]
		if ok == false {
			m[target-nums[i]] = i
		} else {
			return []int{m[nums[i]], i}
		}
	}
	return []int{-1, -1}
}
