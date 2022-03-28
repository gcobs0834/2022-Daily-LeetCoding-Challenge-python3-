class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # We're in left sorted arr
            elif nums[left] < nums[mid]:
                if nums[left] > target or nums[mid] < target:
                    # Search right
                    left = mid + 1
                else:
                    # Search left
                    right = mid - 1
            # We're in right sorted arr
            elif nums[left] > nums[mid]:
                if nums[right] < target or nums[mid] > target:
                    # Search left
                    right = mid - 1
                else:
                    # Search right
                    left = mid + 1
            # Can't decide go left or right, just dummy add 1
            else:
                left += 1
        return False
