/*
 * @lc app=leetcode.cn id=134 lang=cpp
 *
 * [134] Gas Station
 */
#include <unordered_map>
// @lc code=start
class Solution
{
public:
    int canCompleteCircuit1(vector<int> &gas, vector<int> &cost)
    {
        int n = gas.size();
        int i = 0;
        while (i < n)
        {
            int sumOfGas = 0, sumOfCost = 0;
            int cnt = 0;
            while (cnt < n)
            {
                int j = (i + cnt) % n;
                sumOfGas += gas[j];
                sumOfCost += cost[j];
                if (sumOfCost > sumOfGas)
                {
                    break;
                }
                cnt++;
            }
            if (cnt == n)
            {
                return i;
            }
            else
            {
                i = i + cnt + 1;
            }
        }
        return -1;
    }
    int canCompleteCircuit2(vector<int> &gas, vector<int> &cost)
    {
        int n = gas.size();
        for (int i = 0; i < n; i++)
        {
            int j = i;
            int remain = gas[i];
            while (remain - cost[j] >= 0)
            {
                // 减去花费的加上新的点的补给
                remain = remain - cost[j] + gas[(j + 1) % n];
                j = (j + 1) % n;
                // j 回到了 i
                if (j == i)
                {
                    return i;
                }
            }
            // 最远距离绕到了之前，所以 i 后边的都不可能绕一圈了
            if (j < i)
            {
                return -1;
            }
            // i 直接跳到 j，外层 for 循环执行 i++，相当于从 j + 1 开始考虑
            i = j;
        }
        return -1;
    }
    int canCompleteCircuit(vector<int> &gas, vector<int> &cost)
    {
        int i,len = gas.size();
        i = 0;
        while (i < len && gas[i] < cost[i])
        {
            i++;
        }
        while (i < len)
        {
            int gc = gas[i] - cost[i];
            if (gc < 0)
            {
                while (i < len && gas[i] < cost[i])
                {
                    i++;
                }
                continue;
            }
            int j;
            for (j = i + 1; j < len + i; j++)
            {
                int t = j % len;
                gc += gas[t] - cost[t];
                if (gc < 0)
                {
                    if (t < i)
                    {
                        return -1;
                    }
                    i = t;
                    break;
                }
            }
            if (gc >= 0)
            {
                return i;
            }
            i++;
        }
        return -1;
    }
};
// @lc code=end
