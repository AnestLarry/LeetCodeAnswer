/*
 * @lc app=leetcode.cn id=204 lang=csharp
 *
 * [204] Count Primes
 */
//  Count the number of prime numbers less than a non-negative number, n.

//  Example:

//  Input: 10
//  Output: 4
//  Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
// @lc code=start
public class Solution {
    public int CountPrimes (int n) {
        // Accepted
        // 20/20 cases passed (72 ms)
        // Your runtime beats 78.23 % of csharp submissions
        // Your memory usage beats 55.56 % of csharp submissions (16.5 MB)
        if (n <= 2) {
            return 0;
        }
        bool[] res = new bool[n];
        int s = 0;
        Array.Fill (res, true);
        res[0] = false;
        res[1] = false;
        for (int i = 2; i < Math.Sqrt (n) + 1; i++) {
            if (res[i]) {
                for (int j = i + i; j < n; j += i) {
                    res[j] = false;
                }
            }
        }
        foreach (bool b in res) {
            if (b) {
                s++;
            }
        }
        return s;
    }
}
// @lc code=end