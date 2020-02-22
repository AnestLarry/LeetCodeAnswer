/*
 * @lc app=leetcode.cn id=75 lang=golang
 *
 * [75] 颜色分类
 */

// @lc code=start
func sortColors(nums []int) {
	// Accepted
	// 87/87 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 15.3 % of golang submissions (2.1 MB)
	l, r, c := 0, len(nums)-1, 0
	for c <= r {
		if nums[c] == 0 {
			if nums[l] != nums[c] {
				nums[l], nums[c] = nums[c], nums[l]
			}
			l++
			c++
		} else if nums[c] == 2 {
			if nums[c] != nums[r] {
				nums[c], nums[r] = nums[r], nums[c]
			}
			r--
		} else {
			c++
		}
	}
}

// @lc code=end
