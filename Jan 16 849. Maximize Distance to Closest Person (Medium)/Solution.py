class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seats = seats
        lastOneIdx = -1
        maxLen = 0
        
        for idx, seat in enumerate(seats):
            if seat == 1:
                maxLen = max(maxLen, idx if lastOneIdx < 0 else (idx - lastOneIdx) // 2) # init len would be first 1 beacuse we may sit idx 0
                lastOneIdx = idx
        return max(maxLen, len(seats) - 1 - lastOneIdx)# if final seat not 1 update length if we sit in last seat if it is 1 the len is 0
