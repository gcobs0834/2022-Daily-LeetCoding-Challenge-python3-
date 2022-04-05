**[LeetCode Disscuss Post](https://leetcode.com/problems/container-with-most-water/discuss/1915870/PythonGo-2-Different-Solutions-and-Explanations)**
# [Python/Go] 🌟 2 Different Solutions and Explanations 💕

## 1️⃣ Brute Force Approach (❌TLE):
A brute force approach is to genearate all combinations of left and right border.

**Algo**
1. Nested loop left and right, to generate all possibility
2. The **length** of a area is **right - left**, And waterHeight would be **min(height[left], height[right])**
3. Update maxWater = max(maxWater, waterHeight * length)

## Complexity Analysis
* Time: O(N^2): Let N be length of height. We use nested for loop to iterate through every combinations
* Space: O(1)
## Code
**Python**
```python
# Brute Force O(N^2)| O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        for left in range(len(height)):
            for right in range(left + 1, len(height)):
                length = right - left
                waterHeight = min(height[left], height[right])
                maxWater = max(maxWater, waterHeight * length)
        return maxWater
```
**Go**
```go
// Brute Force O(N^2)| O(1)
func maxArea(height []int) int {
    maxWater := 0
    for left := 0; left < len(height); left++{
        for right := left + 1; right < len(height); right++{
            length := (right - left)
            waterHeight := height[left]
            if height[right] < waterHeight{
                waterHeight = height[right]
            }
            area := length * waterHeight
            if area > maxWater{
                maxWater = area
            }
        }
    }
    return maxWater
}
```
## 2️⃣ Two Pointer Approach (✅):
A greedy way to solve this question is to use two pointer approach to shrink the left and right to find maxArea.
Since a water **area = height * length**. We know that the maximum length would be the length of heights
So we could decrease length by making left or right pointer forward. And try to maximize hieght and area.
In that way we could find a maximum area of this question.

**Algo**
1. Init left, right = 0, len(height) - 1, and use while loop to loops through height.
2. Update maxWater = max(maxWater, area)
3. left++ if  height[left] < height[right] else right--
Because our goal is to find **maximum height** to update maxWater

## Complexity Analysis
* Time: O(N): Let N be length of nums
* Space: O(1)
## Iterative Code
**Python**
```python
# Two Pointer O(N) | O(1)
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxWater = 0
        left, right = 0, len(height) - 1
        while left < right:
            area = (right - left) * min(height[left], height[right])
            maxWater = max(maxWater, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
```
**Go**
```go
// Two Pointer O(N) | O(1)
func maxArea(height []int) int {
    maxWater := 0
    left, right := 0, len(height) - 1
    for left < right{
        length := (right - left)
        waterHeight := height[left]
        if height[right] < waterHeight{
            waterHeight = height[right]
            right--
        } else{
            left++
        }
        area := length * waterHeight
        if area > maxWater{
                maxWater = area
            }
    }
    return maxWater
}
```


* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
