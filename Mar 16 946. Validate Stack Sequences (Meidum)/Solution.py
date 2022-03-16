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
