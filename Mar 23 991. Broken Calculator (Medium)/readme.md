**[LeetCode Discuss Post](https://leetcode.com/problems/broken-calculator/discuss/1876653/pythongo-greedy-recursive-and-iterative-solutions-and-explanations)**
# [Python/GO/C++] 🌟 Greedy Recursive and Iterative Solutions and Explanations 💕
## 1️⃣ Recursive Approach:
Simply backtrack target to startValue
1. If target is even, divide by 2 (for startValue multiply the number on display by 2)
2. If target is odd, add 1 (subtract 1 from the number on display.)

**Edge Case**
Once target is less or equal to startValue, means we can obtain the number only by subtract 1 from startValue to target
=> Return startValue - target, to find steps
## Complexity Analysis
* Time: O(logN): Let N be target's number.
* Space: O(logN): Recurrsive call stack.

## Code

**Python**
```python
# Recursive
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # Once target <= startValue, we only do subtract 1 to fit the target
        if target <= startValue:
            return startValue - target
        # Base Greedy Condition
        if target % 2 == 0:
            return 1 + self.brokenCalc(startValue, target // 2)
        else:
            return 1 + self.brokenCalc(startValue, target + 1)
```
**Go**
```go
// Recursive
func brokenCalc(startValue int, target int) int {
    // Once target <= startValue, we only do subtract 1 to fit the target
    if target <= startValue{
        return startValue - target
    }
    // Base Condition
    if target % 2 == 0{
        return 1 + brokenCalc(startValue, target / 2)
    } else{
        return 1 + brokenCalc(startValue, target + 1)
    }
}
```
**C++**
```cpp
// Recursive
class Solution {
public:
    int brokenCalc(int startValue, int target) {
        // Once target <= startValue, we only do subtract 1 to fit the target
        if (target <= startValue){
            return startValue - target;
        }
        // Base Condition
        if (target % 2 == 0){
            return 1 + brokenCalc(startValue, target / 2);
        } else{
            return 1 + brokenCalc(startValue, target + 1);
        }
    }
};
```

## 2️⃣ Iterative Approach:
Same apporach to recurrsive but less space memory. Because we don't use recursive stack.

## Complexity Analysis
* Time: O(logN): Let N be target's number.
* Space: O(1)

## Code

**Python**
```python
# Iterative
class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        steps = 0
        while target > startValue:
            steps += 1
            # Base Greedy Condition
            if target % 2 == 0:
                target //= 2
            else:
                target += 1
        # Once target <= startValue, we only do subtract 1 to fit the target
        return steps + startValue - target
```
**Go**
```go
// Iterative
func brokenCalc(startValue int, target int) int {
    steps := 0
    for target > startValue{
        steps++
        // Base Condition
        if target % 2 == 0{
            target /= 2 
        } else{
            target += 1
        }
    }
    // Once target <= startValue, we only do subtract 1 to fit the target
    return steps + startValue - target
}
```
**C++**
```cpp
// Iterative
class Solution {
public:
    int brokenCalc(int startValue, int target) {
        int steps = 0;
        // Base Condition
        while (target > startValue){
            steps++;
            if (target % 2 == 0){
                target /= 2;
            } else{
                target++;
            }
        }
        // Once target <= startValue, we only do subtract 1 to fit the target
        return steps + startValue - target;
    }
};
```
* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
