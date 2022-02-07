class Solution:
    def addBinary(self, a: str, b: str) -> str:
        idx_a = len(a) - 1
        idx_b = len(b) - 1
        output = ''
        carryIn = 0
        
        while idx_a >= 0 or idx_b >= 0:
            a_digit = int(a[idx_a]) if idx_a >= 0 else 0
            b_digit = int(b[idx_b]) if idx_b >= 0 else 0 
            _sum = (a_digit + b_digit + carryIn) % 2
            carryIn = (a_digit + b_digit + carryIn) // 2
            output = str(_sum) + output
            idx_a -= 1
            idx_b -= 1
            
        if carryIn:
            output = str(carryIn) + output
        
        return output
