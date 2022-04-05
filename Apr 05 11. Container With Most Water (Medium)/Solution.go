// Brute Force O(N^2)| O(1)
func maxArea(height []int) int {
    maxWater := 0
    for left := 0; left < len(height); left++{
        for right := left + 1; right < len(height); right++{
            length := (right - left)
            waterHeight := height[left]
            if height[right] < waterHeight{
                waterHeight = height[right]
            }
            area := length * waterHeight
            if area > maxWater{
                maxWater = area
            }
        }
    }
    return maxWater
}

// Two Pointer O(N) | O(1)
func maxArea(height []int) int {
    maxWater := 0
    left, right := 0, len(height) - 1
    for left < right{
        length := (right - left)
        waterHeight := height[left]
        if height[right] < waterHeight{
            waterHeight = height[right]
            right--
        } else{
            left++
        }
        area := length * waterHeight
        if area > maxWater{
                maxWater = area
            }
    }
    return maxWater
}
