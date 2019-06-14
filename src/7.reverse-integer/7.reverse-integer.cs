/*
 * @lc app=leetcode id=7 lang=csharp
 *
 * [7] Reverse Integer
 Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output: 321
Example 2:

Input: -123
Output: -321
Example 3:

Input: 120
Output: 21
Note:
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.
√ Accepted
  √ 1032/1032 cases passed (40 ms)
  √ Your runtime beats 94.55 % of csharp submissions
  √ Your memory usage beats 31.05 % of csharp submissions (13.2 MB)
 */
public class Solution {
    public int Reverse(int x) {
        bool smollerzero = false;
        string s = x.ToString();
        int l=s.Length, p=0 ,res=0;
        double seq=0.0;
         checked { 
             try { 
                while (p<l){
                if ( s[p] == '-' ){
                    smollerzero=true;
                    p++;
                    continue;
                }
                res+= Convert.ToInt32( int.Parse(s[p].ToString()) * Convert.ToInt32(Math.Pow(10.0,seq)) );
                seq+=1.0;
                p++;
                }
                if(smollerzero){
                    res*=-1;
                }
            } catch (OverflowException oEx) {
               return 0; 
            } 
        }
        return res;
    }
}

