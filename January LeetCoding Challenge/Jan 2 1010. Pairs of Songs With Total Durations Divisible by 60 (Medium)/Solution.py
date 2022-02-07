class Solution:
    def numPairsDivisibleBy60(self, times: List[int]) -> int:
        timeMap = [0  for _ in range(60)]
        outputNum = 0
        for time in times:
            target = (60 - time % 60) % 60
            outputNum += timeMap[target]           
            timeMap[time % 60] += 1
        return outputNum
