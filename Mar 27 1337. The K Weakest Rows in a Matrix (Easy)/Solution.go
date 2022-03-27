// Linear Search, Sort O(M*N + MlogM) ) | O(M) Approach 1 ---------------------------------------------
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

// Binary Search, Sort O(MlogN + MlogM) ) | O(M) Approach 2 ---------------------------------------------
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

// Binary Search, Heap O(MlogN + MlogM) ) | O(M) Approach 3 ---------------------------------------------
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

// MaxHeap and Reverse Heap O(MlogN + Mlogk) ) | O(M) Approach 4 ---------------------------------------------

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

// Traverse Col by cols O(M * N) | O(k) Approach 5 ---------------------------------------------
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


