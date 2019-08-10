/*
 * @lc app=leetcode id=153 lang=csharp
 *
 * [153] Find Minimum in Rotated Sorted Array
 */
//  Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

// Find the minimum element.

// You may assume no duplicate exists in the array.

// Example 1:

// Input: [3,4,5,1,2] 
// Output: 1
// Example 2:

// Input: [4,5,6,7,0,1,2]
// Output: 0
// √ Accepted
//   √ 146/146 cases passed (92 ms)
//   √ Your runtime beats 92.98 % of csharp submissions
//   √ Your memory usage beats 91.67 % of csharp submissions (22.3 MB)
public class Solution {
    public int FindMin(int[] nums) {
        int l = nums.Length;
        if(l<2){
            return nums[0];
        }
        int last=l-1,i=l-1;
        while(i!=-1 && nums[i]<=nums[last]){
            last=i;
            i--;
        }
        return nums[last];
    }
}

