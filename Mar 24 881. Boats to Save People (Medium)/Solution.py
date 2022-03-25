class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort people
        people.sort()
        # Init parameters
        res = 0
        left, right = 0, len(people) - 1
        # Two Pointer iteration
        while left <= right:
            # If we can fit two people in same boat
            if people[right] + people[left] <= limit:
                left += 1
            res += 1
            right -= 1
        return res
