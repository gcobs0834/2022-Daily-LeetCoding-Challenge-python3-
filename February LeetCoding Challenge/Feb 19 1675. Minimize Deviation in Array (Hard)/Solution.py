# Using Heap
class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        newNums = []
        minValue = float('inf')
        # Make all nums even first
        # We make nums negative because build-in api heapq is a min heap, so we convert it to max heap
        for num in nums:
            if num % 2 == 0:
                newNums.append(-num)
                minValue = min(minValue, num)
            else:
                newNums.append(-num * 2)
                minValue = min(minValue, num * 2)
        heapq.heapify(newNums)
        minDeviation = float('inf')
        while newNums:
            curr = -heapq.heappop(newNums) # Find maximum
            minDeviation = min(minDeviation, curr - minValue)
            
            if curr % 2 == 0:
                minValue = min(minValue, curr // 2)
                heapq.heappush(newNums, -curr // 2)
            else:
                break
        return minDeviation
