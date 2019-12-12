/*
 * @lc app=leetcode.cn id=4 lang=golang
 *
 * [4] Median of Two Sorted Arrays
 */
/*There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5*/

// @lc code=start
func findMedianSortedArrays(nums1 []int, nums2 []int) float64 {
	// Accepted
	// 2085/2085 cases passed (12 ms)
	// Your runtime beats 95.6 % of golang submissions
	// Your memory usage beats 34.65 % of golang submissions (6 MB)
	i, j, n, il, jl := 0, 0, 0, len(nums1), len(nums2)
	l := il + jl
	nums := make([]int, l)
	for i < il && j < jl {
		if nums1[i] < nums2[j] {
			nums[n] = nums1[i]
			i, n = i+1, n+1
		} else {
			nums[n] = nums2[j]
			j, n = j+1, n+1
		}
	}
	if i < il {
		nums1 = nums1
	} else {
		nums1, i = nums2, j
	}

	for n < l {
		nums[n] = nums1[i]
		i, n = i+1, n+1
	}
	if l%2 == 0 {
		return float64(nums[(int)(l/2)]+nums[(int)(l/2-1)]) / 2
	} else {
		return float64(nums[(int)(l/2)])
	}

}

// @lc code=end
