class Solution: # O(log n)
    def bitwiseComplement(self, n: int) -> int:
        if not n: return 1
        mask = 1
        leftMost = n
        while leftMost:
            mask = (mask << 1)
            leftMost >>= 1
        mask -= 1
        return mask ^ n

# class Solution: # O(1)
#     def bitwiseComplement(self, n):
# 		return ((2 << int(math.log(max(n, 1), 2))) - 1) - n
#         # return ((2 << int(math.log(max(n, 1), 2))) - 1) ^ n

