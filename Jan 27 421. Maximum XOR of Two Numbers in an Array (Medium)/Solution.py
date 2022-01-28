class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        
        length = len(bin(max(nums))) - 2 #0b1111
        max_xor = 0
        for i in range(length)[::-1]:
            max_xor <<= 1
            curr_xor = max_xor | 1
            prefixes = {num >> i for num in nums}
            max_xor |= any(curr_xor^p in prefixes for p in prefixes)
            
        return max_xor
