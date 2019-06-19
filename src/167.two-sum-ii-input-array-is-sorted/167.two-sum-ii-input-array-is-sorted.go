/*
 * @lc app=leetcode id=167 lang=golang
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
//  √ Accepted
//   √ 17/17 cases passed (4 ms)
//   √ Your runtime beats 98.84 % of golang submissions
//   √ Your memory usage beats 44.52 % of golang submissions (3 MB)
func twoSum(numbers []int, target int) []int {
	l := len(numbers)
	if l < 3 {
		return []int{1, 2}
	}
	i, j, r := 0, l-1, 0
	for i < j {
		r = numbers[i] + numbers[j]
		if r == target {
			return []int{i + 1, j + 1}
		} else if r > target {
			j -= 1
		} else {
			i += 1
		}
	}
	return []int{1, 2}
}
