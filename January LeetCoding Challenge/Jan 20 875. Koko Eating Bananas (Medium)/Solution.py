class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # Applying binary search
        left, right = 1, max(piles)
        res = right
        while left <= right:
            mid = (right + left) // 2
            if self.canEatAll(piles, mid, h):
                res = min(mid, res)  # If can eat them all update res
                right = mid - 1 # Explore left
            else:
                left = mid + 1 # k is too small explore right
        return res
            

    def canEatAll(self, piles, k, h):
        countHours = 0
        for pile in piles:
            countHours += (pile // k) + (pile % k > 0)
            if countHours > h:
                return False
        return True
            
