func search(nums []int, target int) bool {
    left, right := 0, len(nums) - 1
    for left <= right{
        mid := (left + right) / 2
        if nums[mid] == target{
            return true
        //  We're in left sorted arr
        } else if nums[left] < nums[mid]{
            if nums[left] > target || nums[mid] < target{
                // Search right
                left = mid + 1
            } else{
                // Search left
                right = mid - 1
            }
        // We're in right sorted arr
        } else if nums[left] > nums[mid]{
            if nums[right] < target || nums[mid] > target{
                // Search left
                right = mid - 1
            } else{
                // Search right
                left = mid + 1
            }
        // Can't decide go left or right, just dummy add 1
        } else{
            left++
        }
    }
    return false
}
