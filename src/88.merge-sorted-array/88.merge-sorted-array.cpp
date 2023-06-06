/*
 * @lc app=leetcode.cn id=88 lang=cpp
 *
 * [88] 合并两个有序数组
 */
// @lc code=start
class Solution
{
public:
    void merge(vector<int> &nums1, int m, vector<int> &nums2, int n)
    {
        if (n == 0)
        {
            return;
        }
        if (m == 0)
        {
            for (int i = 0; i < n; i++)
            {
                nums1[i] = nums2[i];
            }
            return;
        }
        for (int i = 0; i < n; i++)
        {
            insert(nums1,m+i,nums2[i]);
        }
    }

    void insert(vector<int> &nums1, int max, int value)
    {
        int i;
        for ( i = 0; i < max; i++)
        {
            if (nums1[i] > value)
            {
                int j = max - 1;
                while (j >= i)
                {
                    nums1[j + 1] = nums1[j];
                    j--;
                }
                nums1[i] = value;
                break;
            }
        }
        if (i == max)
        {
            nums1[max] = value;
        }
    }
};
// @lc code=end
