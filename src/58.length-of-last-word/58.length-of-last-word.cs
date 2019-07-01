/*
 * @lc app=leetcode id=58 lang=csharp
 *
 * [58] Length of Last Word
 */
//  Given a string s consists of upper/lower-case alphabets and empty space characters ' ', return the length of last word in the string.

// If the last word does not exist, return 0.

// Note: A word is defined as a character sequence consists of non-space characters only.

// Example:

// Input: "Hello World"
// Output: 5
//  √ Accepted
//   √ 59/59 cases passed (88 ms)
//   √ Your runtime beats 19.39 % of csharp submissions
//   √ Your memory usage beats 5 % of csharp submissions (21.2 MB)
public class Solution {
    public int LengthOfLastWord(string s) {
        s=s.Trim();
        int l = s.Length;
        if (Checkword(s)){
            try{
                return l-s.LastIndexOf(" ")-1;
            }catch{
                return l;
            }
        }
        return 0;
    }
    public bool Checkword(string s){
        string word = "abcdefghijklmnopqrstuvwxyz";
        int l =word.Length;
        for (int i =0 ; i<l;i++){
            if(s.Contains(word[i])){
                return true;
            }
        }
        return false;
    }
}
