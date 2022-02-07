# Python 3 Solution Time: O(N) Space: O(1) 
## Main Idea
We iterate through whole arr **one pass** and see if there are any element violates the base rules

We initial isIncreasing = True, and peak = -1(index)
In the main loop
> Case 1: arr[i] == arr[i -1] means this arr are not strictly increasing or decreasing => return False
> Case 2: Once find a element is smaller than previous means that previous idx is our peak => isIncreasing = False and peak = i - 1
> Case 3 : If we are on decreasing and find a pair is greater than previous one which violates the rule => Return False
> Finally : return isIncreasing == False and peak != 0 (In case the arr is (strictly increasing or strictly decreasing) not a mountains)

## Complexity Analysis
* Time: O(n) : Let *n* be the length of the arr
* Space: O(1)

# [941. Valid Mountain Array](https://leetcode.com/problems/valid-mountain-array/)

Given an array of integers arr, return true if and only if it is a valid mountain array.

Recall that arr is a mountain array if and only if:

arr.length >= 3
There exists some i with 0 < i < arr.length - 1 such that:
arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

## Example 1:

Input: arr = [2,1]
Output: false
## Example 2:

Input: arr = [3,5,5]
Output: false
## Example 3:

Input: arr = [0,3,2,1]
Output: true
 

Constraints:

1 <= arr.length <= 104
0 <= arr[i] <= 104
