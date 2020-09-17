/*
 * @lc app=leetcode.cn id=202 lang=java
 *
 * [202] Happy Number
 */
// Write an algorithm to determine if a number is "happy".

// A happy number is a number defined by the following process: Starting with any positive integer, replace the number by the sum of the squares of its digits, and repeat the process until the number equals 1 (where it will stay), or it loops endlessly in a cycle which does not include 1. Those numbers for which this process ends in 1 are happy numbers.

// Example:

// Input: 19
// Output: true
// Explanation:
// 12 + 92 = 82
// 82 + 22 = 68
// 62 + 82 = 100
// 12 + 02 + 02 = 1
// @lc code=start
class Solution {
    public boolean isHappy(int n) {
// Accepted
// 401/401 cases passed (1 ms)
// Your runtime beats 100 % of java submissions
// Your memory usage beats 18.14 % of java submissions (37.1 MB)
        HashSet repeat = new HashSet();
        repeat.add(n);
        while(n!=1){
            int nn = 0;
            while(n>0){
                int d = n%10;
                nn += d*d;
                n =n/ 10;
            }
            if(repeat.contains(nn)){
                return false;
            }else{
                repeat.add(nn);
            }
            n=nn;
        }
        return true;
    }
}
// @lc code=end

