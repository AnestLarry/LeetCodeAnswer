/*
 * @lc app=leetcode id=88 lang=golang
 *
 * [88] Merge Sorted Array
 */
//  Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

// Note:

// The number of elements initialized in nums1 and nums2 are m and n respectively.
// You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
// Example:

// Input:
// nums1 = [1,2,3,0,0,0], m = 3
// nums2 = [2,5,6],       n = 3

// Output: [1,2,2,3,5,6]
//  √ Accepted
//   √ 59/59 cases passed (0 ms)
//   √ Your runtime beats 100 % of golang submissions
//   √ Your memory usage beats 62.91 % of golang submissions (3.6 MB)
func merge(nums1 []int, m int, nums2 []int, n int) {
	end := len(nums1) - 1
	m, n = m-1, n-1
	for m >= 0 && n >= 0 {
		if nums1[m] > nums2[n] {
			nums1[end] = nums1[m]
			m -= 1
		} else {
			nums1[end] = nums2[n]
			n -= 1
		}
		end -= 1
	}
	if m < 0 {
		i := 0
		for i <= n {
			nums1[i] = nums2[i]
			i += 1
		}
	}
}
