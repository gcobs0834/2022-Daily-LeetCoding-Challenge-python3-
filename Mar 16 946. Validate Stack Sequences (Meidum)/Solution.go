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
