

# Python 3 Solution Time: O(N) Space: O(1) 
## Solution 
Flowers cannot be planted in adjacent plots, which means that every time we see a consecutive 3 zeros we can put a flower in it
So in our algorithm we name a variable count and consecutiveZeros, and looping all flowerbed
### In the main loop
Step 1. If we see a flowerbed is empty we add up consecutiveZeros by 1, if not empty we make consecutiveZeros 0 because we have to recalculate it again
Step 2. Once found 3 consecutiveZeros => count += 1, and consecutiveZeros = 1 [0, 0, 0] =>[0, 1, 0] So consecutiveZeros = 1

Finally: We check if the target value is less our count, and return True or False
## Complexity Analysis
* Time: O(N) : N equals lenghth of flowerbeds
* Space: O(1) We only declare two int variable

# [605. Can Place Flowers](https://leetcode.com/problems/can-place-flowers/)

You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule.

 

# Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
# Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false
 

Constraints:

1 <= flowerbed.length <= 2 * 104
flowerbed[i] is 0 or 1.
There are no two adjacent flowers in flowerbed.
0 <= n <= flowerbed.length
