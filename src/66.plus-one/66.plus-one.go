/*
 * @lc app=leetcode.cn id=66 lang=golang
 *
 * [66] Plus One
 */
//  Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

// The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

// You may assume the integer does not contain any leading zero, except the number 0 itself.

// Example 1:

// Input: [1,2,3]
// Output: [1,2,4]
// Explanation: The array represents the integer 123.
// Example 2:

// Input: [4,3,2,1]
// Output: [4,3,2,2]
// Explanation: The array represents the integer 4321.

// @lc code=start
func plusOne(digits []int) []int {
	// Accepted
	// 109/109 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 65.48 % of golang submissions (2 MB)
	if len(digits) == 1 && digits[0] == 0 {
		return []int{1}
	}
	l := len(digits) - 1
	return add(digits, l)
}

func add(arr []int, p int) []int {
	for {
		if p < 0 {
			r := make([]int, 1)
			r[0] = 1
			r = append(r, arr...)
			return r
		}
		arr[p] += 1
		if arr[p] < 10 {
			break
		} else {
			arr[p] -= 10
			p--
		}
	}
	return arr
}

// @lc code=end
