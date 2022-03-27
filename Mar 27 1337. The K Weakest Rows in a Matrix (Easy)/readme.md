**[LeetCode Disscuss Post](https://leetcode.com/problems/the-k-weakest-rows-in-a-matrix/discuss/1888004/PythonGo-5-Different-Solutions-and-Explanations)**
# [Python/Go] 🌟 5️⃣ Different Solutions and Explanations 💕

## 1️⃣ Linear Search And Sort Approach:
**Algo**
1. Sum Up every row's **1**, and append rowIdx and count in countRow -> O(M * N)
2. Sort by counts and return first k element -> O(MlogM)

## Complexity Analysis
* Time: O(M * N + MlogM)) : M == mat.length, N == mat[i].length
* Space: O(M)
## Code
**Python**
```python
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
```
**Go**
```go
// Linear Search, Sort O(M*N + MlogM) ) | O(M)
func kWeakestRows(mat [][]int, k int) []int {
    countRow := make([][]int, 0)
    for rowIdx, row := range(mat){
        count := 0
        for _, num := range(row){
            count += num
        }
        countRow = append(countRow, []int{rowIdx, count})
    }
    
    sort.Slice(countRow, func(i, j int)bool{
        if countRow[i][1] == countRow[j][1]{
            return countRow[i][0] < countRow[j][0]
        }
        return countRow[i][1] < countRow[j][1]
    })
    res := make([]int, k)
    for i:=0; i < k; i++{
        res[i] = countRow[i][0]
    }
    return res
}
```
## 2️⃣ Binary Search And Sort Approach:
Since sum up all **1** in a row had to traverse whole array. But since all left part are 1, we could use binary search to find the index where first **0** apper. That will be count of 1s

**Algo**
1. Use binary Search to count **1s**
2. Sort by counts and return first k element

## Complexity Analysis
* Time: O(MlogN + MlogM) ): M == mat.length, N == mat[i].length
* Space: O(M)
## Iterative Code
**Python**
```python
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
```
**Go**
```go
// Binary Search, Sort O(MlogN + MlogM) ) | O(M)
func kWeakestRows(mat [][]int, k int) []int {
    countRow := make([][]int, 0)
    for rowIdx, row := range(mat){
        count := binarySearch(row)
        countRow = append(countRow, []int{rowIdx, count})
    }
    
    sort.Slice(countRow, func(i, j int)bool{
        if countRow[i][1] == countRow[j][1]{
            return countRow[i][0] < countRow[j][0]
        }
        return countRow[i][1] < countRow[j][1]
    })
    res := make([]int, k)
    for i:=0; i < k; i++{
        res[i] = countRow[i][0]
    }
    return res
}

func binarySearch(arr []int) int{
    left, right := 0, len(arr) - 1
    for left <= right{
        mid := (left + right) / 2
        if arr[mid] == 1{
            left = mid + 1
        } else{
            right = mid - 1
        }
    }
    return left
}
```

## 3️⃣ Binary Search And Heap Approach:
Instead of sorting after counting all rows. We could use a heap / priority queue to store all counts and rowIdx which compare by its counts
**Algo**
1.1 Use binary Search to count **1s**
1.2 Push **(count and rowIdx)** into heap
2. Return first k element in the priority queue

## Complexity Analysis
* Time O(MlogN + MlogM)): M == mat.length, N == mat[i].length
* Space O(M)
## Code
**Python**
```python
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
```
**Go**
```go
// Binary Search, Heap O(MlogN + MlogM) ) | O(M)
//---------Build a Heap---------//
type Item struct {
    idx  int
    count int
}

type ItemHeap []Item

func (h ItemHeap) Len() int { return len(h) }

func (h ItemHeap) Less(i, j int) bool {
    if h[i].count != h[j].count {
        return h[i].count < h[j].count
    } else {
        return h[i].idx < h[j].idx
    }
}

func (h ItemHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *ItemHeap) Push(val interface{}) {
    *h = append(*h, val.(Item))
}

func (h *ItemHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}
//---------- Solution -----------//
func kWeakestRows(mat [][]int, k int) []int {
    queue := &ItemHeap{}
    for rowIdx, row := range(mat){
        count := binarySearch(row)
        heap.Push(queue, Item{
            idx: rowIdx,
            count: count,
        })
    }
    res := make([]int , k)
    for i :=0; i < k; i++{
        item := heap.Pop(queue).(Item)
        res[i] = item.idx
    }
    return res
}

func binarySearch(arr []int) int{
    left, right := 0, len(arr) - 1
    for left <= right{
        mid := (left + right) / 2
        if arr[mid] == 1{
            left = mid + 1
        } else{
            right = mid - 1
        }
    }
    return left
}
```

## 4️⃣ MaxHeap and Reverse Heap Approach:
We could make a slightly improvement for previous approach.
Since we only return k elements, we actually don't have to store every element in our priority queue.
We can pop the element once the current queue's length exceeds k
**Note**: The top of a heap will return a max/min value. The remaining k element in our priority queue will be the weakest row.
So that is we have to pop all counts are greater than the value in priority queue, so we implement a **MaxHeap** to pop all strong rows.

**Algo**
1.1 Use binary Search to count **1s**
1.2 Push **(count and rowIdx)** into heap if len(heap) < k or count < heap.top
1.3 Once len(haep) > k, pop element with maximum counts of **1**
2. Now our priority queue will be descending order, we have to reverse it and return
## Complexity Analysis
* Time O(MlogN + Mlogk)): M == mat.length, N == mat[i].length
* Space O(k)
## Code
**Python**
```python
# MaxHeap and Reverse Heap O(MlogN + Mlogk) ) | O(k)
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
```
**Go**
```go
// MaxHeap and Reverse Heap O(MlogN + Mlogk) ) | O(k)

//---------Build a maxHeap--------------
type Item struct {
    idx  int
    count int
}

type ItemHeap []Item

func (h ItemHeap) Len() int { return len(h) }
// Change Less function to Max heap
func (h ItemHeap) Less(i, j int) bool {
    if h[i].count != h[j].count {
        return h[i].count >= h[j].count
    } else {
        return h[i].idx >= h[j].idx
    }
}

func (h ItemHeap) Swap(i, j int) { h[i], h[j] = h[j], h[i] }

func (h *ItemHeap) Push(val interface{}) {
    *h = append(*h, val.(Item))
}

func (h *ItemHeap) Pop() interface{} {
    old := *h
    n := len(old)
    x := old[n-1]
    *h = old[0 : n-1]
    return x
}
//---------- Solution -----------//
func kWeakestRows(mat [][]int, k int) []int {
    queue := &ItemHeap{}
    for rowIdx, row := range(mat){
        count := binarySearch(row)
        if queue.Len() < k || count < (*queue)[0].count{
            heap.Push(queue, Item{
            idx: rowIdx,
            count: count,
            })
        }
        if queue.Len() > k{
            heap.Pop(queue)
        }

    }
    res := make([]int , k)
    for i :=0; i < k; i++{
        item := heap.Pop(queue).(Item)
        res[k - i - 1] = item.idx
    }
    return res
}

func binarySearch(arr []int) int{
    left, right := 0, len(arr) - 1
    for left <= right{
        mid := (left + right) / 2
        if arr[mid] == 1{
            left = mid + 1
        } else{
            right = mid - 1
        }
    }
    return left
}
```

## 5️⃣ Greedy Traverse Col by Cols Approach:
The greedy way to solve this problem is to check the value col by cols.
If we find a column with **0**, that means this is a weaker row compare to others with a **1**. So we append row into res and continue.
There is a case that res not equals to k after we finished all Traverse, that is there are rows with all **1**
For example
```
mat = [[1,1,0],[1,1,0],[1,1,1],[1,1,1],[0,0,0],[1,1,1],[1,0,0]]
6
```
We have to count row 2 [1,1,1] and row 5 [1,1,1] in the final result


**Algo**
1.Traverse col by cols
	* If we find a zero, we have to make sure this is our first time append current row in res, so we check if mat[row][col - 1] != 0.
	* If len(res) == k => A early return for res
2. If len(res) < k
	* Traverse from first row to check if its final col will be 1, if so append it in res untill its length match k

## Complexity Analysis
* Time O(M * N) : M == mat.length, N == mat[i].length
* Space O(k)
## Code
**Python**
```python
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
```
**Go**
```go
// Traverse Col by cols O(M * N) | O(k)
func kWeakestRows(mat [][]int, k int) []int {
    res := make([]int, 0)
    for col := 0; col < len(mat[0]); col++{
        for row := 0; row < len(mat); row++{
            if mat[row][col] == 0{
                if col == 0 || mat[row][col - 1] == 1{
                    res = append(res, row)
                }
                if len(res) == k{
                    return res
                }
            }
        }
    }
    
    for row := 0; row < len(mat); row++{
        if mat[row][len(mat[row]) - 1] == 1{
            res = append(res, row)
        }
        if len(res) == k{
            break
        }
    }
    return res
}
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
