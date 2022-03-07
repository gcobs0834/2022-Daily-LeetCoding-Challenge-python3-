class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        
        hashSum = {}
        for i in nums1:
            for j in nums2:
                hashSum[i + j] = hashSum.get(i + j, 0) + 1
                
        count = 0
        for i in nums3:
            for j in nums4:
                target = -(i + j)
                count += hashSum.get(target, 0)
                
        return count
        
