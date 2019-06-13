/*
 * @lc app=leetcode id=66 lang=csharp
 *
 * [66] Plus One

 Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.
Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.
√ Accepted
  √ 109/109 cases passed (252 ms)
  √ Your runtime beats 45.66 % of csharp submissions
  √ Your memory usage beats 59.57 % of csharp submissions (28.2 MB)
 */
public class Solution {
    public int[] PlusOne(int[] digits) {
        if (digits == new int[] { 0}) {
            return new int[]  { 1};
        }
        int l = digits.Length-1;
        return add(digits,l);
    }
    public int[] add(int[] arr,int p){
        if (p<0){
            int[] res = new int[arr.Length+1];
            res[0]=1;
            Array.ConstrainedCopy(arr, 0, res, 1, arr.Length);
            return res;
        }
        arr[p]+=1;
        if (arr[p]<10){
            return arr;
        }else{
            arr[p]-=10;
            return add(arr,p-1);
        }
    }
}

