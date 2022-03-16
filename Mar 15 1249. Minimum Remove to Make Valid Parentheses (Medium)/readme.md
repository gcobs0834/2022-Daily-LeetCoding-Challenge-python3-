**[LeetCode Discuss Post](https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/discuss/1851145/pythongo-2-different-solutions-and-explanations)**

# [Python/GO] 🌟 2 Different Solutions and Explanations 💕
## 1️⃣ Stack Approach:
In this approach, we use **index** for every char in string to store in stack and nonValidIdx. Below is my algorithm.

**Algo**
1. Iterate through string
	* If char == "(", append its idx into stack
	* If char == ")", check if stack is empty. If it's empty add its idx in nonValidIdx
2. Pop out all remaining idx in stack and add it in nonValidIdx
3. Create a res list, and iterate through string, if char not in nonValidIdx append it in res
4. Return "".join(res)
## Complexity Analysis
* Time: O(N)
* Space: O(N): Stack may take O(N/2) at worst, and nonValidIdx is same.

## Code

**Python**
```python
# O(N) | O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        nonValidIdx = set()
        # Find invalid ")" store in nonValidIdx
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    nonValidIdx.add(idx)
        # If stack != empty, remaining "(" is nonValidIdx
        for idx in stack:
            nonValidIdx.add(idx)
            
        # Create result list
        res = []
        for idx, char in enumerate(s):
            if idx not in nonValidIdx:
                res.append(char)
                
        return "".join(res)
```
**Go**
```go
// O(N) | O(N)
func minRemoveToMakeValid(s string) string {
    idxStack := make([]int, 0)
    nonValidIdx := make(map[int]bool)
    
    // Find invalid ")" store in nonValidIdx
    for idx, char := range(s){
        if char == '('{
            idxStack = append(idxStack, idx)
        } else if char == ')'{
            if len(idxStack) != 0{
                idxStack = idxStack[:len(idxStack) - 1]
            } else {
                nonValidIdx[idx] = true
            }
        }
    }
    // If stack != empty, remaining "(" is nonValidIdx
    for len(idxStack) != 0{
        nonValidIdx[idxStack[len(idxStack) - 1]] = true
        idxStack = idxStack[:len(idxStack) - 1]
    }
    
    // Create result slice of rune
    res := make([]rune, 0)
    for idx, char := range(s){
        if _ , found := nonValidIdx[idx]; found{
            continue
        }
        res = append(res, char)
    }
    return string(res) 
}
```

## 2️⃣ No Extra Space Solution Approach:
We can easily count all opening "(" into a count var. And then we see ")" decrease count by 1. If count == 0, we simply don't add current char in res
After pop out all invalid ")" we can apply same technique in reverse way.
**Algo**
1. Iterate through string
	* if char == "(", make count += 1, append it in res
	* if char == ")", check if count >0, if so count -= 1 else continue, don't add the invalid ")" in result
	* Append all other char in res
2. If count > 0, means we have invalid (. So Iterate through reversed string
	* if char == ")", make count += 1, append it in res
	* if char == "(", check if count >0, if so count -= 1 else continue, don't add the invalid ")" in result
	* Append all other char in res
3. Return "".join(res)
## Complexity Analysis
* Time: O(N): Iterate forward and backword both taks O(N)
* Space: O(N): Althrough we didn't use stack, but output res still O(N)

## Code

**Python**
```python
# O(N) | O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        res = []
        # Poping ")"
        for char in s:
            if char == ")":
                if count > 0:
                    count -= 1
                else:
                    continue
            elif char == "(":
                count += 1
            res.append(char)
        # Popping "(" if count > 0
        if count > 0:
            count = 0
            for i in range(len(res))[::-1]:
                if res[i] == "(":
                    if count > 0:
                        count -= 1
                    else:
                        res[i] = ""
                elif res[i] == ")":
                    count += 1
                    
        return "".join(res)       
```
**Go**
**NOTE** : In golang we can't use a empty rune to replace "(", so we have to renew another slice of rune to store final result
```go
// O(N) | O(N)
func minRemoveToMakeValid(s string) string {
    count := 0
    popingLeft := make([]rune, 0)
    // Poping ")"
    for _, char := range(s){
        if char == ')'{
            if count == 0{
                continue
            } else {
                count -= 1
            }
        } else if char == '('{
            count += 1
        }
        popingLeft = append(popingLeft, char)
    }
    
    
    // Poping "(" if count >0 else return string(popingLeft)
    if count > 0{
        count = 0
        res := make([]rune, 0)
        for i := len(popingLeft) - 1; i > -1; i--{
            if popingLeft[i] == '('{
                if count == 0{
                    continue
                } else {
                    count -=1
                }
            } else if popingLeft[i] == ')'{
                count += 1
            }
            res = append(res, popingLeft[i])
        }
        // Reverse res
        for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
            res[i], res[j] = res[j], res[i]
        }
        return string(res)
    }else{
        
        return string(popingLeft)
    }
}
```


* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
