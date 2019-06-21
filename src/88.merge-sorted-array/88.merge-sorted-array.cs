/*
 * @lc app=leetcode id=88 lang=csharp
 *
 * [88] Merge Sorted Array
 */
//  Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

// Note:

// The number of elements initialized in nums1 and nums2 are m and n respectively.
// You may assume that nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.
// Example:

// Input:
// nums1 = [1,2,3,0,0,0], m = 3
// nums2 = [2,5,6],       n = 3

// Output: [1,2,2,3,5,6]
//  √ Accepted
//   √ 59/59 cases passed (252 ms)
//   √ Your runtime beats 54.4 % of csharp submissions
//   √ Your memory usage beats 6.74 % of csharp submissions (28.8 MB)
public class Solution {
    public void Merge(int[] nums1, int m, int[] nums2, int n) {
        int end = nums1.Length-1;
        m = m-1;
        n=n-1;
        while (m>=0 && n >=0){
            if (nums1[m]>nums2[n]){
                nums1[end]=nums1[m];
                m-=1;
            }else{
                nums1[end]=nums2[n];
                n-=1;
            }
            end-=1;
        }
        if(m<0){
            for (int i=0;i<n+1;i++){
                nums1[i]=nums2[i];
            }
        }
    }
}
