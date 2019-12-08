/*
 * @lc app=leetcode id=414 lang=golang
 *
 * [414] Third Maximum Numbe
 */
/*Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.*/
// @lc code=start
func thirdMax(nums []int) int {
	// Accepted
	// 26 / 26 test cases passed (4 ms)
	// Your runtime beats 92.38% of golang submissions
	// Your memory usage beats 100.00% of golang submissions (3 MB)
	max1, max2, max3 := -1<<63, -1<<63, -1<<63
	if len(nums) < 3 {
		Max := nums[0]
		for _, v := range nums {
			if v > Max {
				Max = v
			}
		}
		return Max
	} else {
		for _, v := range nums {
			if v > max1 {
				max1, max2, max3 = v, max1, max2
			} else if max1 != v && v > max2 {
				max3, max2 = max2, v
			} else if max2 != v && v > max3 && max1 > v {
				max3 = v
			}
		}
	}
	if max3 == (-1 << 63) {
		Max := nums[0]
		for _, v := range nums {
			if v > Max {
				Max = v
			}
		}
		return Max
	} else {
		return max3
	}
}

// @lc code=end
