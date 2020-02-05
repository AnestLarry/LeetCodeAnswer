/*
 * @lc app=leetcode.cn id=56 lang=csharp
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
public class Solution
{
    public int[][] Merge(int[][] intervals)
    {
        // Accepted
        // 169/169 cases passed (292 ms)
        // Your runtime beats 98.7 % of csharp submissions
        // Your memory usage beats 30.77 % of csharp submissions (32.3 MB)
        if (intervals == null || intervals.Length < 2) return intervals;
        Array.Sort(intervals, (a, b) => a[0] - b[0]);
        int left = intervals[0][0], right = intervals[0][1];
        List<int[]> res = new List<int[]>();
        for (var i = 1; i < intervals.Length; i++)
        {
            if (intervals[i][0] <= right) //此时必有重合 [1,3],[2,6], 2<3
            {
                right = intervals[i][1] > right ? intervals[i][1] : right;
            }
            else //无重合则直接添加区间
            {
                res.Add(new int[] { left, right });
                left = intervals[i][0];
                right = intervals[i][1];
            }
        }
        res.Add(new int[] { left, right });

        int[][] result = new int[res.Count][];
        for (int i = 0; i < res.Count; i++)
        {
            result[i] = res[i];
        }
        return result;
    }
}
// @lc code=end
