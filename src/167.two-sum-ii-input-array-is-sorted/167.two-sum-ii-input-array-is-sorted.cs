/*
 * @lc app=leetcode id=167 lang=csharp
 *
 * [167] Two Sum II - Input array is sorted
 */
//  Given an array of integers that is already sorted in ascending order, find two numbers such that they add up to a specific target number.

// The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

// Note:

// Your returned answers (both index1 and index2) are not zero-based.
// You may assume that each input would have exactly one solution and you may not use the same element twice.
// Example:

// Input: numbers = [2,7,11,15], target = 9
// Output: [1,2]
// Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
//  √ Accepted
//   √ 17/17 cases passed (264 ms)
//   √ Your runtime beats 40.15 % of csharp submissions
//   √ Your memory usage beats 96.05 % of csharp submissions (29 MB)
public class Solution {
    public int[] TwoSum(int[] numbers, int target) {
        int l =numbers.Length;
        if (l<3){
            return new int[]{1,2};
        }
        int i=0,j=l-1;
        while (i<j){
            int r = numbers[i]+numbers[j];
            if (r==target){
                return new int[]{i+1,j+1};
            }else if(r>target){
                j-=1;
            }else{
                i+=1;
            }
        }
        return new int[]{1,2};
    }
}
