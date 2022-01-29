# Python 3 ✔✔ 3 Different Solution Stack & Two Pointer & DFS

## STACK Solution (OPTIMAL)
We build a stack it stores (startIdx, height) => **startIdx** is idex that corresponding height can **expand from** all the way to final or current index
In the for loop, once we found heights[i] < stack's top's height means we can expand the height in the stack
So we pop out from stack, and check if currentIdx *i* - *startIdx* from stack times height will greater than maxArea

Afer iterate through whole heights, we expand all element from stack to final index and calculate maxArea
## Complexity Analysis
* Time: O(n) : Let *n* be the length of the heights
* Space: O(n): maximum stack will grow if all heights are increasing

## STACK Code
See [Solution.py]()

## Two Pointer (TLE)

That *i* be leftPointer *j* be rightPointer => find min number from left to right and calculate area by minHeight * (i - j + 1)

## Complexity Analysis
* Time: O(n ^ 2) : Let *n* be the length of the heights
* Space: O(1)

## Two Pointer Code
See [Solution.py]()

## DFS (TLE)
### Binary Search Like
Same as previous solution, but we divided each time by finding current local Min height, and expand left and right to find next local minimum to calculate maxArea

## Complexity Analysis
* Time: O(n log n) : Let *n* be the length of the heights
* Space: O(log n): Recurrsive call stack

## DFS Code
See [Solution.py]()

# [84. Largest Rectangle in Histogram](https://leetcode.com/problems/largest-rectangle-in-histogram/)

Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

 

## Example 1:


Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.
## Example 2:


Input: heights = [2,4]
Output: 4
 

Constraints:

1 <= heights.length <= 105
0 <= heights[i] <= 104

