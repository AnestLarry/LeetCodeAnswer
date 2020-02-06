/*
 * @lc app=leetcode.cn id=57 lang=csharp
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
public class Solution {
    public int[][] Insert2 (int[][] intervals, int[] newInterval) {
        // Accepted
        // 154/154 cases passed (300 ms)
        // Your runtime beats 94.87 % of csharp submissions
        // Your memory usage beats 35 % of csharp submissions (32.6 MB)        bool flag = false;
        bool flag = false;
        List<int[]> itvls = new List<int[]> { };
        for (int i = 0; i < intervals.Length; i++) {
            if (intervals[i][0] > newInterval[0]) {
                itvls.Add (new int[] { newInterval[0], newInterval[1] });
                i--;
                newInterval[0] = ~(1 << 31);
                flag = true;
            } else {
                itvls.Add (intervals[i]);
            }
        }
        if (flag == false) {
            itvls.Add (newInterval);
        }

        return Merge (itvls.ToArray ());
    }

    public int[][] Insert (int[][] intervals, int[] newInterval) {
        // Accepted
        // 154/154 cases passed (304 ms)
        // Your runtime beats 89.74 % of csharp submissions
        // Your memory usage beats 50 % of csharp submissions (32.6 MB)
        int[][] i = new int[intervals.Length + 1][];
        for (int j = 0; j < intervals.Length; j++) {
            i[j] = intervals[j];
        }
        i[i.Length - 1] = newInterval;
        Array.Sort (i, (a, b) => a[0] - b[0]);
        return Merge (i);
    }

    public int[][] Merge (int[][] intervals) {
        int left = intervals[0][0], right = intervals[0][1];
        List<int[]> res = new List<int[]> ();
        for (var i = 1; i < intervals.Length; i++) {
            if (intervals[i][0] <= right) {
                right = intervals[i][1] > right ? intervals[i][1] : right;
            } else {
                res.Add (new int[] { left, right });
                left = intervals[i][0];
                right = intervals[i][1];
            }
        }
        res.Add (new int[] { left, right });

        int[][] result = new int[res.Count][];
        for (int i = 0; i < res.Count; i++) {
            result[i] = res[i];
        }
        return result;
    }
}
// @lc code=end