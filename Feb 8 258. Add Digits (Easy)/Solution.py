# Iterative O(log(10)^2) | O(log(10))
class Solution:
    def addDigits(self, num: int) -> int:       
        while len(str(num)) > 1:
            digits = [int(i) for i in str(num)]
            num = sum(digits)
        return num
# Math O(1) | O(1)   
class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9
# One linear       
class Solution:
    def addDigits(self, num: int) -> int:
        return 1 + (num - 1) % 9 if num else 0
