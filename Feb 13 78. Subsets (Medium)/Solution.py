class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]] # Init res set be a empty set
        for num in nums: # Each time add 1 element
            newArr = []
            for item in res: # Copy original in res and put num in
                newArr.append(item + [num])
            res += newArr
        return res
