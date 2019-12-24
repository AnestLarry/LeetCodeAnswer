/*
 * @lc app=leetcode.cn id=33 lang=c
 *
 * [33] Search in Rotated Sorted Array
 */
// Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

// (i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

// You are given a target value to search. If found in the array return its index, otherwise return -1.

// You may assume no duplicate exists in the array.

// Your algorithm's runtime complexity must be in the order of O(log n).

// Example 1:

// Input: nums = [4,5,6,7,0,1,2], target = 0
// Output: 4
// Example 2:

// Input: nums = [4,5,6,7,0,1,2], target = 3
// Output: -1
// @lc code=start

int search(int *nums, int numsSize, int target)
{
    // Accepted
    // 196/196 cases passed (4 ms)
    // Your runtime beats 90.29 % of c submissions
    // Your memory usage beats 67.76 % of c submissions (7.3 MB)
    if (numsSize < 1)
    {
        return -1;
    }
    else if (numsSize < 2)
    {
        return nums[0] == target ? 0 : -1;
    }

    int i = 0;
    for (i = 0; i < numsSize; i++)
    {
        if (nums[i] < nums[0])
            break;
    }
    merge_sort(nums,numsSize);
    int result = -1, left = 0, right = numsSize - 1;
    while(left<=right){
        int mid = (left+right)>>1;
        if(nums[mid]==target){
            result = mid+i;
            if(result>numsSize-1 && i!=0){
                return result-numsSize;
            }
            return result;
        }
        if(nums[mid]<target){
            left= mid+1;
        }else{
            right = mid-1;
        }
    }
    return result;
}


int min(int x, int y) {
    return x < y ? x : y;
}
void merge_sort(int arr[], int len) {
    int* a = arr;
    int* b = (int*) malloc(len * sizeof(int));
    int seg, start;
    for (seg = 1; seg < len; seg += seg) {
        for (start = 0; start < len; start += seg + seg) {
            int low = start, mid = min(start + seg, len), high = min(start + seg + seg, len);
            int k = low;
            int start1 = low, end1 = mid;
            int start2 = mid, end2 = high;
            while (start1 < end1 && start2 < end2)
                b[k++] = a[start1] < a[start2] ? a[start1++] : a[start2++];
            while (start1 < end1)
                b[k++] = a[start1++];
            while (start2 < end2)
                b[k++] = a[start2++];
        }
        int* temp = a;
        a = b;
        b = temp;
    }
    if (a != arr) {
        int i;
        for (i = 0; i < len; i++)
            b[i] = a[i];
        b = a;
    }
    free(b);
}

// @lc code=end
