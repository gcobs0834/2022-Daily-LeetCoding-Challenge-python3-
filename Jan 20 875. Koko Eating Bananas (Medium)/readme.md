# Python 3 Solution Time: O(N log(m)) Space: O(1) 
## Main Idea

A naive approach to solve this question is to brute force all k value from 1 to max value of piles. It takes O(n* m) wher *n* be the length of the input array and *m* be the maximum number of bananas in a single pile

But clearly we can improve this by applying binary search in it

> Step 1: Find middle of left and right value (Init by 1 and max(piles)
> Step 2: Check if the mid value can eat all bananas in time h
> Step 2.1 : If it **CAN** eat all of them in time => we update res by the min value of res and mid, and move **right** to **mid - 1** explore left part of mid
> Step 2.2 : If it **can't** eat all of them in time => Move **left** to **mid + 1** explore right part of mid
> Step 3: repeate 1 ~ 2 until left > right and return res


## Complexity Analysis
* Time: O(n log(m)) : Let *n* be the length of the input array pilespiles and *m* be the maximum number of bananas in a single pile from pilespiles.
* Space: O(1)

# [875. Koko Eating Bananas](https://leetcode.com/problems/koko-eating-bananas/)

Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

 

# Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4
# Example 2:

Input: piles = [30,11,23,4,20], h = 5
Output: 30
# Example 3:

Input: piles = [30,11,23,4,20], h = 6
Output: 23
 

Constraints:

1 <= piles.length <= 104
piles.length <= h <= 109
1 <= piles[i] <= 109
