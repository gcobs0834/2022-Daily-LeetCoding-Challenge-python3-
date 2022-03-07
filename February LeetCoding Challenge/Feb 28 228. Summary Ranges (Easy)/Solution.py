# O(N) | O(1)
class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums: return []
        # Init parameters currRange = [startPoint, endPoint]
        res = []
        currRange = [nums[0], nums[0]]
        
        for i in range(1, len(nums)):
            # Once nums are not consecutive, update res and reinit currRange
            if nums[i] != nums[i - 1] + 1:
                self.updateSummary(currRange, res)
                currRange = [nums[i], nums[i]]
            # Update endPoint
            else:
                currRange[1] = nums[i]
                
        # Update res again to append final range
        self.updateSummary(currRange, res)
        return res
    
    def updateSummary(self, currRange, summary):
        # Case 1: "a" if a == b
        if currRange[0] == currRange[1]:
            summary.append(str(currRange[0]))
        # Case 2: "a->b" if a != b
        else:
            summary.append("{}->{}".format(currRange[0], currRange[1]))
