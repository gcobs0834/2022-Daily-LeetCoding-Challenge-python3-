class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if not n: return 1
        mask = 1
        leftMost = n
        while leftMost:
            mask = (mask << 1)
            leftMost >>= 1
        mask -= 1
        return mask ^ n
