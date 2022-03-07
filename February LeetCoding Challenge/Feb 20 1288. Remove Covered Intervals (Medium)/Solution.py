# Naive Approach O(NlogN)|O(N)
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:    
        intervals.sort(key = lambda x: x[0])        
        lastInterval = intervals[0]
        count = 1
        for i in range(1, len(intervals)):
            # Basic logic
            if intervals[i][1] <= lastInterval[1]:
                continue
            # In case both inverval share same start point, we update lastInterval
            elif intervals[i][0] == lastInterval[0] and lastInterval[1] <= intervals[i][1]:
                lastInterval = intervals[i]
                continue
            # Update last interval and increase count
            lastInterval = intervals[i]
            count += 1
        return count
# Improved Approach O(NlogN)|O(N)
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # To deal with edge case, we sort both (x[0] and -x[1])
        intervals.sort(key = lambda x: (x[0], -x[1]))
        lastInterval = intervals[0]
        count = 1
        for i in range(1, len(intervals)):
            # Basic logic
            if intervals[i][1] <= lastInterval[1]:
                continue
            # Update last interval and increase count
            lastInterval = intervals[i]
            count += 1
        return count
