/*
 * @lc app=leetcode id=345 lang=csharp
 *
 * [345] Reverse Vowels of a String
 */
// Write a function that takes a string as input and reverse only the vowels of a string.

// Example 1:

// Input: "hello"
// Output: "holle"
// Example 2:

// Input: "leetcode"
// Output: "leotcede"
// Note:
// The vowels does not include the letter "y".


// @lc code=start
public class Solution
{
    public string ReverseVowels(string s)
    {
        // Accepted
        // 481/481 cases passed (144 ms)
        // Your runtime beats 5.9 % of csharp submissions
        // Your memory usage beats 25 % of csharp submissions (27.7 MB)
        char[] vowels = "AEIOUaeiou".ToCharArray(), schars = s.ToCharArray();
        int i = 0, l = s.Length;
        List<char> chars = new List<char> { };
        foreach (char c in schars)
        {
            if (vowels.Contains(c))
            {
                chars.Add(c);
            }
        }
        int chars_length = chars.Count() - 1;
        if (chars.Count() > 0)
        {
            while (i < l)
            {
                if (vowels.Contains(schars[i]))
                {
                    schars[i] = chars[chars_length];
                    chars_length --;
                }
                i++;
            }
        }
        return string.Join("", schars);
    }
}
// @lc code=end

