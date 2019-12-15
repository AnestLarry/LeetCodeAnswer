/*
 * @lc app=leetcode.cn id=8 lang=golang
 *
 * [8] String to Integer (atoi)
 # Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:

# Input: "42"
# Output: 42
# Example 2:

# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:

# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:

# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:

# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

*/

// @lc code=start
func myAtoi(str string) int {
	// Accepted
	// 1079/1079 cases passed (0 ms)
	// Your runtime beats 100 % of golang submissions
	// Your memory usage beats 77.01 % of golang submissions (2.3 MB)
	var res, ind int64 = 0, 1
	cur := 0
	if len(str) < 1 {
		return 0
	}
	for ; cur < len(str) && str[cur] == ' '; cur++ {
	}
	if cur < len(str) && (str[cur] == '-' || str[cur] == '+') {
		if str[cur] == '-' {
			ind = -1
		}
		cur += 1
	}
	for cur < len(str) && '0' <= str[cur] && str[cur] <= '9' {
		res = res*10 + int64(str[cur]-'0')
		cur += 1
		if res*ind > (1<<31)-1 || res*ind < (-1<<31) {
			if res*ind > (1<<31)-1 {
				return (1 << 31) - 1
			}
			return (-1 << 31)
		}

	}
	return int(res * ind)
}

// @lc code=end
