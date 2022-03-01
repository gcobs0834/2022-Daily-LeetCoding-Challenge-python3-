# Count 1s O(N logN) |O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:     
        res = [0] * (n + 1)
        for x in range(n + 1):
            res[x] = self.count1s(x)
        return res
    
    def count1s(self, n):
        count = 0
        while n != 0:
            n &= n - 1
            count += 1
        return count

# DP O(N) | O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        offset = 1
        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i
            res[i] = 1 + res[i - offset]
        return res

# DP Shift right O(N) | O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i >> 1] + (i & 1)
        return res

# DP Shift right O(N) | O(N)
class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = 1 + res[i & (i-1)]
        return res
