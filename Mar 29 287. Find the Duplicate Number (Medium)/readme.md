**[LeetCode Disscuss Post](https://leetcode.com/problems/find-the-duplicate-number/discuss/1893643/pythongo-3-different-solutions-and-explanations)**
# [Python/Go] 🌟 3 Different Solutions and Explanations 💕
Approach 1 and Approach 2 doesn't follow the restriction
**You must solve the problem without modifying the array nums and uses only constant extra space.**

## 1️⃣ Counter Set Approach (❌Extra Space):
Simply creat a hashMap to check whether current number is in our hashmap. If so, we find duplicate number.

## Complexity Analysis
* Time: O(N): Let N be length of nums
* Space: O(N): For counter set at worst take O(N)
## Code
**Python**
```python
# Counter Set O(N) | O(N)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = set()
        for num in nums:
            if num in counter:
                return num
            counter.add(num)
```
**Go**
```go
/* Counter Set O(N) | O(N) */
func findDuplicate(nums []int) int {
    counter := make(map[int]bool)
    for _, num := range(nums){
        if _, found := counter[num]; found{
            return num
        }
        counter[num] = true
    }
    return -1
}
```
## 2️⃣ Index as a Hash Key. Approach (❌Modifying the Array):
See [41. First Missing Positive](https://leetcode.com/problems/first-missing-positive/), Since nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
We could make certain index's number negative to represent that current number had been visited.
Next time if we visit this index's number find its negative means we found duplicate.

**Algo**
1. targetIdx = abs(num) - 1 (0-index, so [1,n] would be maps to [0, n-1])
2. If nums[targetIdx] <0, visited this num return targetIdx + 1 (We don't return num because num could be negative targetIdx is more straightforward)
	* Else num[targetIdx] * = -1

## Complexity Analysis
* Time: O(N): Let N be length of nums
* Space: O(1)
## Iterative Code
**Python**
```python
# Negative Marking O(N) | O(1)
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        for num in nums:
            # Find targetIdx
            targetIdx = abs(num) - 1
            # If already negative means duplicate
            if nums[targetIdx] < 0:
                return targetIdx + 1
            else:
                nums[targetIdx] *= -1
```
**Go**
```go
// /* Negative Marking O(N) | O(1) */
func findDuplicate(nums []int) int {
    for _, num := range(nums){
        // abs for num
        if num < 0 {
            num *= - 1 
        }
        // Find targetIdx
        targetIdx := num - 1
        // If already negative means duplicate
        if nums[targetIdx] < 0{
            return targetIdx + 1
        }
        // Make neagative
        nums[targetIdx] *= -1
    }
    return -1
}
```

## 3️⃣ Binary Search Approach:
The way to implement binaray search. Would be counting the numbers before mid value
For example
```
nums = [1,3,4,2,2] , left = 0, right = 4
1. mid = 2 => The numbers <= 2 is 3.
It means we have duplicate number which is smaller than 2. So we search left. Right = 2 - 1
2. mid = 1 => The numbers <= 1 is 1.
It means all value from 1 to 1 would not be duplicates
```
By applying binary search, We could provide a solution without modifying the array nums and uses only constant extra space.

**Algo**
1. Init left and right
2. Binary Search
	* Count the numbers in nums <= mid.
	* If count > mid:
	Set duplicate = left, and search left
	* Else:
	Search right to find duplicates

## Complexity Analysis
* Time: O(N logN): Let N be length of nums
* Space: O(1)
## Code
**Python**
```python
# Binary Search (NlogN) | O(1)     
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            # Count numbers <= mid
            count = sum(num <= mid for num in nums)
            if count > mid:
                duplicate = mid
                right = mid - 1
            else:
                left = mid + 1
        return duplicate
```
**Go**
```go
/* Binary Search (NlogN) | O(1) */
func findDuplicate(nums []int) int {
    left, right := 0, len(nums) - 1
    duplicate := 0
    for left <= right{
        mid := (left + right) / 2
        count := 0
        // Count numbers <= mid
        for _,num := range(nums){
            if num <= mid{
                count++
            }
        }
        // Search left
        if count > mid{
            duplicate = mid
            right = mid - 1
        } else { // Search right
            left = mid +1
        }      
    }
    return duplicate
}
```


* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
