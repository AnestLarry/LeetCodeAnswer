#
# @lc app=leetcode id=917 lang=python3
#
# [917] Reverse Only Letters
#
# Given a string S, return the "reversed" string where all characters that are not a letter stay in the same place, and all letters reverse their positions.


# Example 1:

# Input: "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"


# Note:

# S.length <= 100
# 33 <= S[i].ASCIIcode <= 122
# S doesn't contain \ or "
import string


class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        # √ Accepted
        #   √ 116/116 cases passed (32 ms)
        #   √ Your runtime beats 92.99 % of python3 submissions
        #   √ Your memory usage beats 5.56 % of python3 submissions (13.9 MB)
        al = string.ascii_letters
        letter: list[str] = [x for x in S if x in al]
        sl = list(S.replace("\"", "").replace("\\", ""))
        print(S, sl)
        for i in range(len(sl)):
            if sl[i] in al:
                sl[i] = letter.pop()
        return "".join(sl)
