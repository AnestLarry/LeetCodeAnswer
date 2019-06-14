/*
 * @lc app=leetcode id=50 lang=csharp
 *
 * [50] Pow(x, n)
 Implement pow(x, n), which calculates x raised to the power n (xn).

Example 1:

Input: 2.00000, 10
Output: 1024.00000
Example 2:

Input: 2.10000, 3
Output: 9.26100
Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2-2 = 1/22 = 1/4 = 0.25
Note:

-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [−231, 231 − 1]
√ Accepted
  √ 304/304 cases passed (72 ms)
  √ Your runtime beats 6.15 % of csharp submissions
  √ Your memory usage beats 65.9 % of csharp submissions (13.2 MB)
 */
public class Solution {
    public double MyPow(double x, int n) {
        //return Math.Pow(x,n);
        double res=1.0;
        if (x==1.0){
            return 1.0;
        }else if(x==-1.0){
            if (n%2==0){
                return 1.0;
            }
            return -1.0;
        }
        checked { 
            try { 
                if (n<0){
                    x = 1/x;
                    n*=-1;
                }
                while(n>0 && Math.Round(res,5)!=0.0){
                  res*=x;
                  n-=1;
                }
                return res;
            } catch (OverflowException oEx) {
                return 0.0;
            } 
        }
    }
}
