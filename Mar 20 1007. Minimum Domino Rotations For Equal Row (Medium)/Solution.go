func minDominoRotations(tops []int, bottoms []int) int {
    res := -1
    // Loops through tops[0] or bottoms[0]
    for _, val := range([]int{tops[0], bottoms[0]}){
        isValid := true
        swapTopCnt, swapBottomCnt := 0, 0
        for idx:= 0; idx < len(tops); idx++{
            if tops[idx] == val && bottoms[idx] == val{
                continue
            // Count if we have to  Swap Top to Bottom
            } else if tops[idx] == val {
                swapTopCnt += 1
            // Count if we have to  Swap Bottom to Top
            } else if bottoms[idx] == val{
                swapBottomCnt += 1
            // If not valid, don't update res
            } else{
                isValid = false
                break
            }
        }
        // Check whether make all top value equal, or bottom value equal takes minimum swaps
        if isValid{
            if res == -1{
                res = swapTopCnt
            }
            if swapTopCnt < res{
                res = swapTopCnt
            }
            if swapBottomCnt < res{
                res = swapBottomCnt
            }
        }
    }
    
    return res
}
