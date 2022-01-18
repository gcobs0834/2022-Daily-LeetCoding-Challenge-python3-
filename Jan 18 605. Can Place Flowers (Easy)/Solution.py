class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0] #If first two or last two index be zero, append one zero so our algorithm could fit in
        count, consecutiveZeros = 0, 0
        
        for flower in flowerbed:
            if flower == 0:
                consecutiveZeros += 1 
                if consecutiveZeros == 3: # Once found 3 consecutiveZeros => count += 1, and consecutiveZeros = 1
                    count +=1
                    consecutiveZeros = 1
            else:
                consecutiveZeros = 0
                
        return n <= count
