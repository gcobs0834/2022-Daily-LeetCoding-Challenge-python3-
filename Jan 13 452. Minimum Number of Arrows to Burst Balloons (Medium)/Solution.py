class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        sortedPoints = sorted(points, key = lambda x: x[1])
        arrowsCount, arrowPos = 0, float("-inf")
        
        for interval in sortedPoints:
            start, end = interval
            if start > arrowPos:
                arrowsCount += 1
                arrowPos = end
                
        return arrowsCount
