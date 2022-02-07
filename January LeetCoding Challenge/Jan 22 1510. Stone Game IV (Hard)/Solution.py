# Top-Down Recursive
import math
class Solution:
    def winnerSquareGame(self, n: int) -> bool:

        def SquareGameHelper(n, cache):
            if n == 0 :
                return False
            if n in cache:
                return cache[n]

            squareUpperBound = (math.isqrt(n))  #isqrt will sqrt n and floor it down
            for i in range(1, squareUpperBound + 1):
                newN = n - (i*i)
                cache[newN] = SquareGameHelper(newN, cache)
                if not cache[newN]: return True
            cache[n] = False
            return cache[n]
        
        return SquareGameHelper(n, {})
    
# Bottom-Up Dp Solution
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        
        win = [False] * (n+1) # init 0~N to be False means if win[n] == False means must lose
        for i in range(1, n + 1):
            for j in range(1, int(i**0.5) + 1):
                if win[i - j**2] == False:
                    win[i] = True
                    break
        return win[n]
        
        
        
        
        
