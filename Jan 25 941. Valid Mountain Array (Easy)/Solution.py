class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3: # Base case must len >= 3
            return False
        
        isIncreasing = True
        peak = -1
        
        for i in range(1, len(arr)):
            if arr[i] == arr[i -1]: # Not strictly increasing or decreasing
                return False
            
            if isIncreasing and arr[i] < arr[i - 1]: # Find peak
                peak = i - 1
                isIncreasing = False
                
            if not isIncreasing and arr[i] > arr[i - 1]:
                return False
            
        return isIncreasing == False and peak != 0
