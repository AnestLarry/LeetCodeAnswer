/*
 * @lc app=leetcode id=414 lang=csharp
 *
 * [414] Third Maximum Number
 */
// @lc code=start
/*Given a non-empty array of integers, return the third maximum number in this array. If it does not exist, return the maximum number. The time complexity must be in O(n).

Example 1:
Input: [3, 2, 1]

Output: 1

Explanation: The third maximum is 1.
Example 2:
Input: [1, 2]

Output: 2

Explanation: The third maximum does not exist, so the maximum (2) is returned instead.
Example 3:
Input: [2, 2, 3, 1]

Output: 1

Explanation: Note that the third maximum here means the third maximum distinct number.
Both numbers with value 2 are both considered as second maximum.*/
public class Solution
{
    public int ThirdMax(int[] nums)
    {
        // Accepted
        // 26 / 26 test cases passed (96 ms)
        // Your runtime beats 81.65% of csharp submissions
        // Your memory usage beats 100.00% of csharp submissions (24 MB)
        if (nums.Length < 3)
        {
            return nums.Max();
        }
        else
        {
            long max1=long.MinValue,max2=long.MinValue,max3=long.MinValue;
            foreach (var cur in nums)
            {
                if (max1 < cur)
                {
                    max3 = max2;
                    max2 = max1;
                    max1 = cur;
                }
                else if (max1 != cur && max2 < cur)
                {
                    max3 = max2;
                    max2 = cur;
                }
                else if (max2 != cur && cur < max1 && max3 < cur)
                {
                    max3 = cur;
                }
            }
            return (int)(max3 == long.MinValue ? max1 : max3);
        }
    }
    public int ThirdMax2(int[] nums)
    {
        // Accepted
        // 26 / 26 test cases passed (608 ms)
        // Your runtime beats 5.05% of csharp submissions
        // Your memory usage beats 100.00% of csharp submissions (25.7 MB)
        ArrayList al = new ArrayList();
        int Min = nums[0];
        foreach (int i in nums)
        {
            Min = i < Min ? i : Min;
        }
        int[] maxs = new int[3];
        maxs[0] = Min; maxs[1] = Min; maxs[2] = Min;
        foreach (int i in nums)
        {
            bool flag = true;
            foreach (int j in al)
            {
                if (j == i)
                {
                    flag = false;
                }
            }
            if (flag)
            {
                {
                    if (i > maxs[0])
                    {
                        maxs[2] = maxs[1];
                        maxs[1] = maxs[0];
                        maxs[0] = i;
                    }
                    else if (i > maxs[1])
                    {
                        maxs[2] = maxs[1];
                        maxs[1] = i;
                    }
                    else if (i > maxs[2])
                    {
                        maxs[2] = i;
                    }
                }
                al.Add(i);
            }
        }
        int l = 0;
        foreach (int i in al)
        {
            l++;
        }
        if (l < 3)
        {
            int Max = nums[0];
            foreach (int i in al)
            {
                Max = i > Max ? i : Max;
            }
            return Max;
        }
        return maxs[2];
    }
}
// @lc code=end