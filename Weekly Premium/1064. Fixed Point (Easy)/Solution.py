# O(N) | O(1)
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        for i, num in enumerate(arr):
            if i == num:
                return i
        return -1

# O(log N) | O(1)
class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        l, r = 0, len(arr) - 1
        answer = -1
        while l <= r:
            mid = (l + r) // 2
            if mid == arr[mid]:
                answer = mid
                r = mid - 1
            elif mid < arr[mid]:
                r = mid - 1
            else:
                l = mid + 1
        return answer
