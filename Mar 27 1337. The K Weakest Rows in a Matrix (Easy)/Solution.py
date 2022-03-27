# Linear Search, Sort O(M*N + MlogM) ) | O(M)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        countRow = []
        for rowIdx, row in enumerate(mat):
            count = sum(row)
            countRow.append([rowIdx, count])
        countRow.sort(key = lambda x: x[1])
        res = [0] * k
        for i in range(k):
            res[i] = countRow[i][0]    
        return res

# Binary Search, Sort O(MlogN + MlogM) ) | O(M)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        countRow = []
        # Binary Search for each row
        for rowIdx, row in enumerate(mat):
            count = self.binarySearch(row)
            countRow.append([rowIdx, count])
        # Sort countRow
        countRow.sort(key = lambda x: x[1])
        res = [0] * k
        for i in range(k):
            res[i] = countRow[i][0]    
        return res

    # Binary Search
    def binarySearch(self, arr):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == 1:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Binary Search, Heap O(MlogN + MlogM) ) | O(M)
import heapq
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        queue = []
        # Binary Search for each row
        for rowIdx, row in enumerate(mat):
            count = self.binarySearch(row)
            entry = [count , rowIdx]
            heapq.heappush(queue, entry)
                
        res = [0] * k
        for i in range(k):
            count, idx = heapq.heappop(queue)
            res[i] = idx
        return res

    # Binary Search
    def binarySearch(self, arr):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == 1:
                left = mid + 1
            else:
                right = mid - 1
        return left
        
# MaxHeap and Reverse Heap O(MlogN + Mlogk) ) | O(M)
import heapq

class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        queue = []
        # Binary Search for each row
        for rowIdx, row in enumerate(mat):
            count = self.binarySearch(row)
            entry = [-count , -rowIdx]
            if len(queue) < k or entry > queue[0]:
                heapq.heappush(queue, entry)
            if len(queue) > k:
                heapq.heappop(queue)
                
        res = [0] * k
        for i in range(k):
            count, idx = heapq.heappop(queue)
            res[i] = -idx
        return res[::-1]

    # Binary Search
    def binarySearch(self, arr):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == 1:
                left = mid + 1
            else:
                right = mid - 1
        return left

# Traverse Col by cols O(M * N) | O(k)
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        res = []
        for col in range(len(mat[0])):
            for row in range(len(mat)):
                if mat[row][col] == 0:
                    if col == 0 or mat[row][col - 1] != 0:
                        res.append(row)
                if len(res) == k:
                    return res
                
        for row in range(len(mat)):
            if mat[row][-1] == 1:
                res.append(row)
            if len(res) == k:
                return res                 
