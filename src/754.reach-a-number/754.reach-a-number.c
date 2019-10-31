/*
 * @lc app=leetcode id=754 lang=c
 *
 * [754] Reach a Number
 *  https://leetcode.com/problems/reach-a-number/discuss/410112/Python-Solution

 */
// You are standing at position 0 on an infinite number line. There is a goal at position target.

// On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

// Return the minimum number of steps required to reach the destination.

// Example 1:
// Input: target = 3
// Output: 2
// Explanation:
// On the first move we step from 0 to 1.
// On the second step we step from 1 to 3.
// Example 2:
// Input: target = 2
// Output: 3
// Explanation:
// On the first move we step from 0 to 1.
// On the second move we step  from 1 to -1.
// On the third move we step from -1 to 2.
// Note:
// target will be a non-zero integer in the range [-10^9, 10^9].

// @lc code=start
#include <math.h>

int reachNumber(int target)
{
    // Accepted
    // 73/73 cases passed (0 ms)
    // Your runtime beats 100 % of c submissions
    // Your memory usage beats 100 % of c submissions (6.9 MB)
    int res = 0;
    target = abs(target);
    while (target > 0)
    {
        res++;
        target -= res;
    }
    if (target % 2 != 0)
    {
        res += 1 + res % 2;
    }
    return res;
}

// @lc code=end
