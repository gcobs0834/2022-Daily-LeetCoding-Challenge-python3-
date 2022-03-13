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
