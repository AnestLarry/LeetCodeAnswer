import "sort"

/*
 * @lc app=leetcode.cn id=56 lang=golang
 *
 * [56] Merge Intervals
 */
// Given a collection of intervals, merge all overlapping intervals.

// Example 1:

// Input: [[1,3],[2,6],[8,10],[15,18]]
// Output: [[1,6],[8,10],[15,18]]
// Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
// Example 2:

// Input: [[1,4],[4,5]]
// Output: [[1,5]]
// Explanation: Intervals [1,4] and [4,5] are considered overlapping.
// NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.

// @lc code=start

func merge(intervals [][]int) [][]int {
	// Accepted
	// 169/169 cases passed (12 ms)
	// Your runtime beats 80.11 % of golang submissions
	// Your memory usage beats 80.51 % of golang submissions (4.7 MB)
	if intervals == nil || len(intervals) < 2 {
		return intervals
	}
	sort.Sort(ByX(intervals))
	left, right := intervals[0][0], intervals[0][1]
	var res [][]int
	for i := 1; i < len(intervals); i++ {
		if intervals[i][0] <= right {
			if intervals[i][1] > right {
				right = intervals[i][1]
			}
		} else {
			res = append(res, []int{left, right})
			left = intervals[i][0]
			right = intervals[i][1]
		}
	}
	res = append(res, []int{left, right})
	return res
}

type ByX [][]int

func (b ByX) Len() int {
	return len(b)
}

func (b ByX) Swap(i, j int) {
	b[i], b[j] = b[j], b[i]
}

func (b ByX) Less(i, j int) bool {
	return b[i][0] < b[j][0]
}

// @lc code=end
