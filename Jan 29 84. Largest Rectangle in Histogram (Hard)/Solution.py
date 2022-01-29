# Two Pointer
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        for i in range(len(heights)):
            minHeight = float('inf')
            for j in range(i, len(heights)):
                minHeight = min(minHeight, heights[j])
                maxArea = max(maxArea, minHeight * (j - i + 1))
        return maxArea
# DFS
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        return self.calFromMin(0, len(heights) - 1, heights)
    
    def calFromMin(self, startIdx, endIdx, heights):
        if startIdx > endIdx:
            return 0
        minIdx = self.getMinIdx(startIdx, endIdx, heights)
        
        return max(heights[minIdx] * (endIdx - startIdx + 1), 
                   self.calFromMin(startIdx, minIdx - 1, heights), # explore left
                   self.calFromMin(minIdx + 1, endIdx, heights)) # explore right
        
    def getMinIdx(self, startIdx, endIdx, heights):
        currentMin = float('inf')
        minIdx = -1
        for i in range(startIdx, endIdx + 1):
            if heights[i] < currentMin:
                currentMin = heights[i]
                minIdx = i
        return minIdx
      
# Stack     
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0
        for i in range(len(heights)):
            startIdx = i
            while stack and stack[-1][1] > heights[i]:
                idx, height = stack.pop()
                maxArea = max(maxArea, height * (i - idx))
                startIdx = idx
            stack.append((startIdx, heights[i])) # store (idx, height)
        
        for startIdx, height in stack:
            maxArea = max(maxArea, height * (len(heights) - startIdx))
            
        return maxArea
