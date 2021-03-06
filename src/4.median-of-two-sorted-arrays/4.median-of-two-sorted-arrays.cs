/*
 * @lc app=leetcode id=4 lang=csharp
 *
 * [4] Median of Two Sorted Arrays
 */
/*There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5*/
// @lc code=start
public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        // Accepted
        // 2085/2085 cases passed (140 ms)
        // Your runtime beats 91.58 % of csharp submissions
        // Your memory usage beats 5.05 % of csharp submissions (27 MB)
        int i = 0, j = 0, n = 0, il = nums1.Length, jl = nums2.Length, l = il + jl;
        int[] nums = new int[il + jl];
        while (i < il && j < jl)
        {
            if (nums1[i] < nums2[j])
            {
                nums[n] = nums1[i];
                i++; n++;
            }
            else
            {
                nums[n] = nums2[j];
                j++; n++;
            }
        }
        nums1 = i < il ? nums1 : nums2;
        i = i < il ? i : j;
        while (n < l)
        {
            nums[n] = nums1[i];
            i++; n++;
        }
        if (l % 2 == 0)
        {
            return (double)(nums[(int)(l / 2)] + nums[(int)(l / 2 - 1)]) / 2;
        }
        else
        {
            return nums[(int)(l / 2)];
        }
    }
}
// @lc code=end