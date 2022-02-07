class Solution:
    def findFinalValue(self, nums: List[int], original: int) -> int:
        numHash = {}
        for num in nums:
            if num not in numHash:
                numHash[num] = True
        while True:
            if original in numHash:
                original *= 2
            else:
                return original
