// Count 1s O(N logN) |O(N)
func countBits(n int) []int {
    res := make([]int , n + 1)
    for i := 0; i <= n; i++{
        res[i] = count1s(i)
    }
    return res
}

func count1s(n int) int{
    count := 0
    for n != 0{
        count += 1
        n &= (n - 1)
    }
    return count
}

// DP Offset O(N) |O(N)
func countBits(n int) []int {
    res := make([]int , n + 1)
    offset := 1
    for i := 1; i <= n; i++{
        if offset * 2 == i{
            offset = i
        }
        res[i] = 1 + res[i - offset]
    }
    return res
}

// DP Shift right O(N) |O(N)
func countBits(n int) []int {
    res := make([]int , n + 1)
    for i := 1; i <= n; i++{
        res[i] = res[i >> 1] + (i&1)
    }
    return res
}

// DP Shift right O(N) |O(N)
func countBits(n int) []int {
    res := make([]int , n + 1)
    for i := 1; i <= n; i++{
        res[i] = 1 + res[i & (i-1)]
    }
    return res
}
