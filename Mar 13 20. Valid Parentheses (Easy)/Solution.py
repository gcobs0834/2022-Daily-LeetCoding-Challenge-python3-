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
