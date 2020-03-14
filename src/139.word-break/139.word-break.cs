/*
 * @lc app=leetcode id=139 lang=csharp
 *
 * [139] Word Break
 */
/*Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
*/
// @lc code=start
public class Solution {
    public bool WordBreak (string s, IList<string> wordDict) {
        // Accepted
        // 36/36 cases passed (112 ms)
        // Your runtime beats 94.12 % of csharp submissions
        // Your memory usage beats 80 % of csharp submissions (26.4 MB)
        if (wordDict == null) {
            return s == "" ? false : true;
        }
        int l = s.Length;
        bool[] bl = new bool[l + 1];
        bl[0] = true;
        for (int i = 1; i < l + 1; i++) {
            bl[i] = false;
        }
        for (int i = 1; i <= l; i++) {
            for (int j = i - 1; j > -1; j--) {
                if (bl[j] && wordDict.Contains (s.Substring (j, i - j))) {
                    bl[i] = true;
                    break;
                }
            }
        }
        return bl[l];
    }
}
// @lc code=end

