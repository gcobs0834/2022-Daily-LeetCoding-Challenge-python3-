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
