
# 🌟[Python 3] 2 Different Solutions and Explanation (Follow-up)🤠

## 1️⃣ HashMap Approach:
Simply use a hashMap to store every number's **frequency** once it equal **n // 2 + 1** we immediately return it.

## Complexity Analysis
* Time: O(N) : Let N be length of nums
* Space: O(N) :  HashMap, since we have one element's frequency is greater than n // 2, so at worst hashmap store **O(n//2 + 1)** keys


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/a96ca82f9d8fd8a4fde6f6d143f35f169724f62a/Feb%2021%20169.%20Majority%20Element%20(Easy)/Solution.py#L2)

## 2️⃣ Greedy Improved Approach:
**Follow-up: Could you solve the problem in linear time and in O(1) space?**

> We selecte a number as **potential cadiate** and with a **counter**, once we find a different number we decrease counter
> Once we run out our counter means at that moment there is **no element** become majority element. So we can selected a new candidate

## Dry Run

```
nums = [2, 2, 1, 1, 1, 2, 2]
# In for loop
i = 0 => selected = 2, count = 1 # ['2', 2, 1, 1, 1, 2, 2]
i = 1 => selected = 2, count = 2 # [2, '2', 1, 1, 1, 2, 2]
i = 2 => selected = 2, count = 1 # [2, 2, '1', 1, 1, 2, 2] Sees 1 so it become an offset decrease count
i = 3 => selected = 2, count = 0 # [2, 2, 1, '1', 1, 2, 2] Count = 0
i = 4 => selected = 1, count = 1 # [2, 2, 1, 1, '1', 2, 2] Because our count == 0 we renew a candidate
i = 5 => selected = 1, count = 0 # [2, 2, 1, 1, 1, '2', 2] Count = 0
i = 6 => selected = 2, count = 1 # [2, 2, 1, 1, 1, 2, '2'] We selected 2 at final round 
```
## How doese the solution work?
* Because the problem described **You may assume that the majority element always exists in the array.**
* So we know that there is a number its frequency is greater than others, so in this case we know once we scan all elements in nums, the remaining element must have greatest frequency



## Complexity Analysis
* Time: O(N) : Let N be length of nums
* Space: O(1)


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/a96ca82f9d8fd8a4fde6f6d143f35f169724f62a/Feb%2021%20169.%20Majority%20Element%20(Easy)/Solution.py#L11)

## 😎 (Follow up) What if the majority element not necessary exists in array?:
**In this case once we don't find a number that is greaterf than n // 2 +1 we return None**

* This time once we find the number with max frequency. We simply loop through nums again to find if the cadidate's frequency is acutally greater than **N // 2 + 1**, if not we return None

## Complexity Analysis
* Time: O(N) : Let N be length of nums
* Space: O(1) 


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/a96ca82f9d8fd8a4fde6f6d143f35f169724f62a/Feb%2021%20169.%20Majority%20Element%20(Easy)/Solution.py#L23)

# [169. Majority Element](https://leetcode.com/problems/majority-element/)

Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

 

## Example 1:

Input: nums = [3,2,3]
Output: 3
## Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
 

Constraints:

n == nums.length
1 <= n <= 5 * 104
-231 <= nums[i] <= 231 - 1
 

Follow-up: Could you solve the problem in linear time and in O(1) space?

