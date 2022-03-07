# # O(N) | O(N)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numHash = {}
        for num in nums:
            numHash[num] = numHash.get(num, 0) + 1
            if numHash[num] == len(nums) // 2 + 1:
                return num

# O(N) | O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        selected = None
        count = 0
        for num in nums:
            # Move to new selected candidate
            if count == 0:
                selected = num
            count += 1 if selected == num else -1   
        return selected

# O(N) | O(1)
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        selected = None
        count = 0
        for num in nums:
            if count == 0:
                selected = num
                
            if selected == num:
                count += 1
            else:
                if count == 1:
                    selected = None
                count -= 1
        # renew count to check whether selected is autually greater than n // 2 + 1    
        count = 0
        for num in nums:
            if num == selected:
                count += 1
        return selected if count >= len(nums) // 2 + 1 else None
        
                
