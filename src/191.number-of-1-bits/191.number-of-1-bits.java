/*
 * @lc app=leetcode.cn id=191 lang=java
 *
 * [191] 位1的个数
 */
/*
//  Write a function that takes an unsigned integer and return the number of '1' bits it has (also known as the Hamming weight).

// Example 1:

// Input: 00000000000000000000000000001011
// Output: 3
// Explanation: The input binary string 00000000000000000000000000001011 has a total of three '1' bits.
// Example 2:

// Input: 00000000000000000000000010000000
// Output: 1
// Explanation: The input binary string 00000000000000000000000010000000 has a total of one '1' bit.
// Example 3:

// Input: 11111111111111111111111111111101
// Output: 31
// Explanation: The input binary string 11111111111111111111111111111101 has a total of thirty one '1' bits.

// Note:

// Note that in some languages such as Java, there is no unsigned integer type. In this case, the input will be given as signed integer type and should not affect your implementation, as the internal binary representation of the integer is the same whether it is signed or unsigned.
// In Java, the compiler represents the signed integers using 2's complement notation. Therefore, in Example 3 above the input represents the signed integer -3.

// Follow up:

// If this function is called many times, how would you optimize it?

Accepted
601/601 cases passed (1 ms)
Your runtime beats 99.02 % of java submissions
Your memory usage beats 37.87 % of java submissions (36.7 MB)
*/
// @lc code=start
public class Solution {
    // you need to treat n as an unsigned value
    public int hammingWeight(int n) {
        int r;
        for(r = 0;n!=0;r++){
            n&=n-1;
        }
        return r;
    }
}
// @lc code=end

