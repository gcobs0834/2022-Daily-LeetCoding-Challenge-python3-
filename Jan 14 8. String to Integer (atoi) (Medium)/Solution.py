class Solution:
    def myAtoi(self, s: str) -> int:
        idx = 0
        sign, output = 1, ""
        
        while idx < len(s) and s[idx] == " ": # Step 1 Read in and ignore any leading whitespace.
            idx += 1
                
        if idx < len(s) and (s[idx] == "-" or s[idx] == "+"): # Step 2 Check if the next character (if not already at the end of the string) is '-' or '+'
            sign = int(s[idx] + "1")
            idx += 1
        
        while idx < len(s) and s[idx].isdigit(): # Step 3 Read in next the characters until the next non-digit character or the end of the input is reached.
            output += s[idx]
            idx += 1
                
        output = sign * int(output or 0)
        
        if output <= -2 ** 31: #Final check If the integer is out of the 32-bit signed integer range
            return -2 ** 31
        elif output >= 2**31 - 1:
            return 2 ** 31 -1
        return output
