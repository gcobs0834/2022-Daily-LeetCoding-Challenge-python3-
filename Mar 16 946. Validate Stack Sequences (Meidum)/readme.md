**[LeetCode Dicuss Post](https://leetcode.com/problems/validate-stack-sequences/discuss/1853732/pythongo-stack-two-pointer-solution-and-explanation)**
# [Python/GO/C++] 🌟 Stack Two Pointer Solution and Explanation 💕
## 1️⃣ Main Idea:

**Algo**
1. Init two pointers (pushIdx, popIdx) and stack
2. Iterate through pushed
	 * Append(pushed[pushIdx]) into stack, and increase pushIdx
	 * While top of stack == popped[popIdx] , we pop out top and check next element in popped equals to next top
3. Return if stack is empty, if so means we found valid sequence.

**Note** : It may seems we use **two nested loop**, but at the end we **only** traverse through both pushed and popped.

## Complexity Analysis
* Time: O(N): Let N be the length of pushed and popped.
* Space: O(N): Stack takes at worst all pushed in Stack

## Code

**Python**
```python
# Two pointer O(N) | O(N)
class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        pushIdx, popIdx = 0, 0
        stack = []
        
        # Iterate through pushed
        while pushIdx < len(pushed) and popIdx < len(popped):
            stack.append(pushed[pushIdx])
            pushIdx += 1
            # Once current top == popped[idx], we start pop it and move popIdx forward
            while stack and stack[-1] == popped[popIdx]:
                stack.pop()
                popIdx += 1
        # If stack is not empty means, we cannot pop in the sequences
        return len(stack) == 0
```
**Go**
```go
// Two Pointer O(N) | O(N)
func validateStackSequences(pushed []int, popped []int) bool {
    // Init two pointer and stack
    pushIdx, popIdx := 0, 0
    stack := make([]int, 0)
    
    // Iterate through pushed
    for pushIdx < len(pushed) && popIdx < len(popped){
        stack = append(stack, pushed[pushIdx])
        pushIdx += 1
        // Once current top == popped[idx], we start pop it and move popIdx forward
        for len(stack) != 0 && stack[len(stack) - 1] == popped[popIdx]{
            stack = stack[:len(stack) - 1] // Pop last element
            popIdx += 1
        }
    }
    // If stack is not empty means we cannot find a sequence
    return len(stack) == 0
    
}
```
**C++**
```c++
// Two Pointer O(N) | O(N)
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        // Init two pointer and stack
        stack<int> Stack;
        int pushIdx = 0 , popIdx = 0;
        // Iterate through pushed   
        while (pushIdx < pushed.size() && popIdx < popped.size()){
            Stack.push(pushed[pushIdx]);
            pushIdx++;
            // Once current top == popped[idx], we start pop it and move popIdx forward
            while (!Stack.empty() && Stack.top() == popped[popIdx]){
                Stack.pop();
                popIdx++;
            }
        }
        // If stack is not empty means we cannot find a sequence
        return Stack.empty();
    }
};
```
* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
