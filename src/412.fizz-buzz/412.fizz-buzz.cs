/*
 * @lc app=leetcode id=412 lang=csharp
 *
 * [412] Fizz Buzz
 */
//  Write a program that outputs the string representation of numbers from 1 to n.

// But for multiples of three it should output “Fizz” instead of the number and for the multiples of five output “Buzz”. For numbers which are multiples of both three and five output “FizzBuzz”.

// Example:

// n = 15,

// Return:
// [
//     "1",
//     "2",
//     "Fizz",
//     "4",
//     "Buzz",
//     "Fizz",
//     "7",
//     "8",
//     "Fizz",
//     "Buzz",
//     "11",
//     "Fizz",
//     "13",
//     "14",
//     "FizzBuzz"
// ]
public class Solution {
    public IList<string> FizzBuzz(int n) {
        // √ Accepted
        // √ 8/8 cases passed (260 ms)
        // √ Your runtime beats 70.07 % of csharp submissions
        // √ Your memory usage beats 40 % of csharp submissions (31.7 MB)
        List<string> result = new List<string>{};
        if(n<1){
            return result;
        }
        for(int i = 1; i < n+1; i++){
            if(i%5==0){
                if(i%3==0){
                    result.Add("FizzBuzz");
                    continue;
                }
                result.Add("Buzz");
            }else if(i%3==0){
                result.Add("Fizz");
            }else{
                result.Add(i.ToString());
            }
        }
        return result;
    }
}
