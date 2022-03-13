**[LeetCode Discuss Post](https://leetcode.com/problems/valid-parentheses/discuss/1846383/pythongo-stack-solution-and-explanation)**
# [Python/GO] 🌟 Stack Solution and Explanation 💕
## 1️⃣ Main Idea:
Using a stack, once find closing parentheses we check if top of stack equals its corresponding pair.
**Algo**
1. Create empty stack, opening and closing hashMap
2. Iterate through string if found opening parentheses append it in stack.
	* If found closing parentheses: Check if stack is empty, and the top of stack would be its pair
3. Return True if stack is empty

**Note :  I know s consists of parentheses only '()[]{}'. But in our code we ignore all other string and only deal with parentheses. It can use for more complex string. Like s = [3 * (7+5)]**
## Complexity Analysis
* Time: O(N): Let N be the length of linked list
* Space: O(N): At worst stack store O(N/2) element. ```[(, (, (, (, ), ), ), )]``` = > stack at worst will be ```[(, (, (, (]```

## Code

**Python**
```python
class Solution(object):
    def isValid(self, s):
        # Creat stack and opening and closing hashmap
        stack = []
        opening = set(['(', '{', '['])
        closing = {'}':'{', ']':'[', ')':'('}
        
        
        for char in s:
            # Append opening parentheses to stack
            if char in opening:
                stack.append(char)
            # Pop parentheses once find a closing parentheses
            elif char in closing:
                # If no corresponding parentheses return False
                if not stack or closing[char] != stack[-1]:
                    return False
                stack.pop()
                
        return not stack
```
**Go**
```go
func isValid(s string) bool {
    // Creat stack and opening and closing hashmap
    stack := make([]rune, 0)
    opening := map[rune]rune{
        '(' : ')',
        '[' : ']',
        '{' : '}',
    }
    closing := map[rune]rune{
        ')' : '(',
        ']' : '[',
        '}' : '{',
    }
    
    for _, char := range s{
        // Append opening parentheses to stack
        if _, found := opening[char]; found{
            stack = append(stack, char)
        // Pop parentheses once find a closing parentheses
        } else if _, found := closing[char]; found{
            // If no corresponding parentheses return False
            if len(stack) == 0 || stack[len(stack) - 1] != closing[char]{
                return false
            }
            stack = stack[:len(stack) - 1]
        }
    }
    return len(stack) == 0
}
```
* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
