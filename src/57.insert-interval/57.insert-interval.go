import "sort"

/*
 * @lc app=leetcode.cn id=57 lang=golang
 *
 * [57] Insert Interval
 */
//  Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

//  You may assume that the intervals were initially sorted according to their start times.

//  Example 1:

//  Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
//  Output: [[1,5],[6,9]]
//  Example 2:

//  Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
//  Output: [[1,2],[3,10],[12,16]]
//  Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].
//  NOTE: input types have been changed on April 15, 2019. Please reset to default code definition to get new method signature.
// @lc code=start
func insert(intervals [][]int, newInterval []int) [][]int {
	// Accepted
	// 154/154 cases passed (8 ms)
	// Your runtime beats 91.97 % of golang submissions
	// Your memory usage beats 47.46 % of golang submissions (4.9 MB)
	flag := false
	for i := 0; i < len(intervals); i++ {
		if intervals[i][0] > newInterval[0] {
			intervals = append(intervals[:i+1],
				intervals[i:]...)
			intervals[i] = newInterval
			flag = true
			break
		}

	}
	if !flag {
		intervals = append(intervals, newInterval)
	}
	return merge(intervals)
}

func merge(intervals [][]int) [][]int {
	sort.Sort(ByX(intervals))
	left, right := intervals[0][0], intervals[0][1]
	res := make([][]int, 0)
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
