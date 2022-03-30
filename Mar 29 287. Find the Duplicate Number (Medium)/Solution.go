/* Counter Set O(N) | O(N) */
func findDuplicate(nums []int) int {
    counter := make(map[int]bool)
    for _, num := range(nums){
        if _, found := counter[num]; found{
            return num
        }
        counter[num] = true
    }
    return -1
}

// /* Negative Marking O(N) | O(1) */
func findDuplicate(nums []int) int {
    for _, num := range(nums){
        // abs for num
        if num < 0 {
            num *= - 1 
        }
        // Find targetIdx
        targetIdx := num - 1
        // If already negative means duplicate
        if nums[targetIdx] < 0{
            return targetIdx + 1
        }
        // Make neagative
        nums[targetIdx] *= -1
    }
    return -1
}

/* Binary Search (NlogN) | O(1) */
func findDuplicate(nums []int) int {
    left, right := 0, len(nums) - 1
    duplicate := 0
    for left <= right{
        mid := (left + right) / 2
        count := 0
        // Count numbers <= mid
        for _,num := range(nums){
            if num <= mid{
                count++
            }
        }
        // Search left
        if count > mid{
            duplicate = mid
            right = mid - 1
        } else { // Search right
            left = mid +1
        }      
    }
    return duplicate
}
