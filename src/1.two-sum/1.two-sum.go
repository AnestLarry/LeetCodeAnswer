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
	i, j, l := 0, 1, len(nums)
	for i < l {
		for j < l {
			if nums[i]+nums[j] == target {
				return []int{i, j}
			}
			j++
		}
		i, j = i+1, i+2
	}
	return []int{l - 1, l}
}