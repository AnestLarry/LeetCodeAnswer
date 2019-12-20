import "sort"

/*
 * @lc app=leetcode.cn id=15 lang=golang
 *
 * [15] 3Sum
 */
/* # Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

# Note:

# The solution set must not contain duplicate triplets.

# Example:

# Given array nums = [-1, 0, 1, 2, -1, -4],

# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]*/
// @lc code=start
func threeSum(nums []int) [][]int {
	// Accepted
	// 313/313 cases passed (32 ms)
	// Your runtime beats 98.55 % of golang submissions
	// Your memory usage beats 100 % of golang submissions (6.9 MB)
	var res [][]int
	sort.Ints(nums)
	l := len(nums)
	for i := 0; i < l-2; i++ {
		if i != 0 && nums[i] == nums[i-1] {
			continue
		}
		last, j := l-1, i+1
		for j < last {
			s := nums[i] + nums[j] + nums[last]
			if s == 0 {
				res = append(res, []int{nums[i], nums[j], nums[last]})
				j++
				last--
				for j != (i+1) && nums[j] == nums[j-1] && j < last {
					j++
				}
				for last != (l-1) && nums[last] == nums[last+1] && last > j {
					last--
				}
			} else {
				if s > 0 {
					last--
				} else {
					j++
				}
			}
		}
	}
	return res
}

// @lc code=end
