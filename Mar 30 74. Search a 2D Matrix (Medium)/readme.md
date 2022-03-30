**[LeetCode Disscuss](https://leetcode.com/problems/search-a-2d-matrix/discuss/1896078/pythongoc-binary-search-solution-and-explanation)**
# [Python/GO/C++] 🌟Binary Search Solution and Explanation 💕
## 1️⃣ Main Idea:
Since the integers in each row are sorted from left to right. The first integer of each row is greater than the last integer of the previous row.
We could assume we squeeze 2D matrix into a 1D array.
For example
```
2D matirx = 
[ 1, 3, 5, 7]
[10,11,16,20]
[23,30,34,60]
1D array = [1, 3, 5, 7, 10, 11,16, 20, 23, 30, 34, 60]
```
In this case, we can apply binary search in the squeeze array.
But we only need to do is turing the binary search's low, high and mid index into 2D matrx's row and col index
We could easily calculate row and col by **Row = mid // N, Col = mid % N**

**Algo**
1. Init parameters M, N, low, high
2. Binary Search
	* mid = low + (high - low) // 2, and calculate mid's row and col index
	* if found target return true
	* else search left or right
3. return false if we can find target in binary search
## Complexity Analysis
* Time: Worst: O(logM * N): M == matrix.length N == matrix[i].length
* Space: O(1)

## Code

**Python**
```python
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        M, N = len(matrix), len(matrix[0])
        low, high = 0, (M * N - 1)
        while low <= high:
            mid = low + (high - low) // 2
            row, col = mid // N, mid % N
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False
```
**Go**
```go
func searchMatrix(matrix [][]int, target int) bool {
    M, N := len(matrix), len(matrix[0])
    low, high := 0, M*N - 1
    for low <= high{
        mid := low + (high - low) / 2
        row, col := mid / N, mid % N
        
        if matrix[row][col] == target{
            return true
        } else if matrix[row][col] < target{
            low = mid + 1
        } else{
            high = mid - 1
        }
    }
    return false
}
```
**C++**
```cpp
class Solution {
  public:
  bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int M = matrix.size(), N = matrix[0].size();

    // binary search
    int low = 0, high = M*N - 1;
    while (low <= high){
        int mid = low + (high - low) / 2;
        int row = mid / N, col = mid % N;
        if (matrix[row][col] == target){
            return true;
        } else if (matrix[row][col] < target){
            low = mid + 1;
        }else{
            high = mid - 1;
        }
    }
    return false;
  }
};
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
