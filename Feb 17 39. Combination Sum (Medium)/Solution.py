class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []
        self.calHelper([], 0, candidates, target, res)
        return res
        
    def calHelper(self, currentList, startIdx, candidates, target, res):
        # Once target == 0 means we found a vaild list
        if target == 0:
            res.append(currentList)
            return
        
        # Start from startIdx means we can use duplicate nums
        for i in range(startIdx, len(candidates)):
            num = candidates[i]
            if num <= target:
                self.calHelper(currentList + [num], i, candidates, target - num, res)
            # Since candidates are sorted, if we cant find a vaild num <= target we break
            else:
                break
