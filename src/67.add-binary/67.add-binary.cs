/*
 * @lc app=leetcode.cn id=67 lang=csharp
 *
 * [67] Add Binary
 */
// Given two binary strings, return their sum (also a binary string).

// The input strings are both non-empty and contains only characters 1 or 0.

// Example 1:

// Input: a = "11", b = "1"
// Output: "100"
// Example 2:

// Input: a = "1010", b = "1011"
// Output: "10101"
// @lc code=start
public class Solution {
    public string AddBinary (string a, string b) {
        // Accepted
        // 294/294 cases passed (100 ms)
        // Your runtime beats 85.71 % of csharp submissions
        // Your memory usage beats 27.38 % of csharp submissions (24.9 MB)
        if (a.Length > b.Length) {
            for (; a.Length > b.Length;) {
                b = "0" + b;
            }
        } else {
            for (; a.Length < b.Length;) {
                a = "0" + a;
            }
        }
        string res = "";
        bool flag = false;
        for (int i = a.Length - 1; - 1 < i; i--) {
            if (a[i] == b[i] && a[i] == '0') {
                res = (flag? "1": "0") + res;
                flag = false;
            } else if (a[i] == b[i] && a[i] == '1') {
                res = (flag? "1": "0") + res;
                flag = true;
            } else {
                res = (flag? "0": "1") + res;
            }
        }
        if (flag) {
            res = "1" + res;
        }
        return res;

    }
}
// @lc code=end