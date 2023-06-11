/*
 * @lc app=leetcode.cn id=6 lang=cpp
 *
 * [6] Zigzag Conversion
 */
#include<string>
// @lc code=start
class Solution {
public:
    string convert(string s, int numRows) {
        int n = s.size();
        if (numRows == 1 || numRows >= n) {
            return s;
        }
        string ans;
        int t = numRows * 2 - 2;
        for (int i = 0; i < numRows; ++i) { // 枚举矩阵的行
            for (int j = 0; j + i < n; j += t) { // 枚举每个周期的起始下标
                ans += s[j + i]; // 当前周期的第一个字符
                if (0 < i && i < numRows - 1 && j + t - i < n) {
                    ans += s[j + t - i]; // 当前周期的第二个字符
                }
            }
        }
        return ans;
    }
    string convert2(string s, int numRows) {
        if (numRows == 1) return s;
        vector<string> rows(numRows);
        // 行转向标志，极妙
        int flag = 1;  
        // 行下标索引
        int idxRows = 0;   
        for (int i = 0; i < s.size(); i++) {
            rows[idxRows].push_back(s[i]);
            // 更新行下标
            idxRows += flag;  
            if (idxRows == numRows - 1 || idxRows == 0) {
                // 转向，上——>下 | 下——>上
                flag = -flag;
            }
        }
        string res;
        for (auto row : rows) {
            // 拿到答案
            res += row;
        }
        return res;
    }
};
// @lc code=end

