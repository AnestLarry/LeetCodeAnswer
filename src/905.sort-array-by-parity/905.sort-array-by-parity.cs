/*
 * @lc app=leetcode id=905 lang=csharp
 *
 * [905] Sort Array By Parity
 */
//  Given an array A of non-negative integers, return an array consisting of all the even elements of A, followed by all the odd elements of A.

// You may return any answer array that satisfies this condition.

// Example 1:

// Input: [3,1,2,4]
// Output: [2,4,3,1]
// The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

// Note:

// 1 <= A.length <= 5000
// 0 <= A[i] <= 5000
//  √ Accepted
//   √ 285/285 cases passed (264 ms)
//   √ Your runtime beats 89.33 % of csharp submissions
//   √ Your memory usage beats 20 % of csharp submissions (32.4 MB)
public class Solution {
    public int[] SortArrayByParity(int[] A) {
        List<int> a = new List<int>{};
        foreach(int i in A){
            if(i%2==0){
                a.Insert(0,i);
            }else{
                a.Add(i);
            }
        }
        return a.ToArray();
    }
}

