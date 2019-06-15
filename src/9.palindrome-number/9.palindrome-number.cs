/*
 * @lc app=leetcode id=9 lang=csharp
 *
 * [9] Palindrome Number
 */
//  Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

// Example 1:

// Input: 121
// Output: true
// Example 2:

// Input: -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
// Follow up:

// Coud you solve it without converting the integer to a string?
//  √ Accepted
//   √ 11509/11509 cases passed (64 ms)
//   √ Your runtime beats 91.76 % of csharp submissions
//   √ Your memory usage beats 100 % of csharp submissions (14.4 MB)
public class Solution {
    public bool IsPalindrome(int x) {
        if(x<0){
            return false;
        }else if(x<10){
            return true;
        }
        int r=0,rx=x;
        while (rx>0){
            r = r*10 + rx%10;
            rx=(int)rx/10;
        }
        if (r == x){
            return true;
        }
        return false;
    }
}

