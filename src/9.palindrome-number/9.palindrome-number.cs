/*
 * @lc app=leetcode id=9 lang=csharp
 *
 * [9] Palindrome Number
 */
//  Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.

// Example 1:

// Input: 121
// Output: true
// Example 2:

// Input: -121
// Output: false
// Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
// Example 3:

// Input: 10
// Output: false
// Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
// Follow up:

// Coud you solve it without converting the integer to a string?
//  √ Accepted
//   √ 11509/11509 cases passed (64 ms)
//   √ Your runtime beats 91.76 % of csharp submissions
//   √ Your memory usage beats 100 % of csharp submissions (14.4 MB)
public class Solution
{
    public bool IsPalindrome(int x)
    {
        // Accepted
        // 11509/11509 cases passed (68 ms)
        // Your runtime beats 97.64 % of csharp submissions
        // Your memory usage beats 24.29 % of csharp submissions (16.6 MB)
        if (x < 0)
        {
            return false;
        }
        string xs = x.ToString(), left, right;
        int l_xs = xs.Length, r_l;
        left = l_xs % 2 != 0 ? xs.Substring(0, l_xs / 2 + 1) : xs.Substring(0, l_xs / 2);
        right = xs.Substring(l_xs / 2);
        r_l = right.Length - 1;
        for (int i = 0; i <= r_l; i++)
        {
            if (right[i] != left[r_l - i])
            {
                return false;
            }
        }
        return true;
    }

    public bool IsPalindrome2(int x)
    {
        // Accepted
        // 11509/11509 cases passed (84 ms)
        // Your runtime beats 64.51 % of csharp submissions
        // Your memory usage beats 81.4 % of csharp submissions (15.2 MB)
        if (x < 0)
        {
            return false;
        }
        else if (x < 10)
        {
            return true;
        }
        int r = 0, rx = x;
        while (rx > 0)
        {
            r = r * 10 + rx % 10;
            rx = (int)rx / 10;
        }
        if (r == x)
        {
            return true;
        }
        return false;
    }
}

