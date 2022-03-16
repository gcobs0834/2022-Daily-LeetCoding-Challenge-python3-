// O(N) | O(N)
func minRemoveToMakeValid(s string) string {
    idxStack := make([]int, 0)
    nonValidIdx := make(map[int]bool)
    
    // Find invalid ")" store in nonValidIdx
    for idx, char := range(s){
        if char == '('{
            idxStack = append(idxStack, idx)
        } else if char == ')'{
            if len(idxStack) != 0{
                idxStack = idxStack[:len(idxStack) - 1]
            } else {
                nonValidIdx[idx] = true
            }
        }
    }
    // If stack != empty, remaining "(" is nonValidIdx
    for len(idxStack) != 0{
        nonValidIdx[idxStack[len(idxStack) - 1]] = true
        idxStack = idxStack[:len(idxStack) - 1]
    }
    
    // Create result slice of rune
    res := make([]rune, 0)
    for idx, char := range(s){
        if _ , found := nonValidIdx[idx]; found{
            continue
        }
        res = append(res, char)
    }
    return string(res) 
}

// O(N) | O(N)
func minRemoveToMakeValid(s string) string {
    count := 0
    popingLeft := make([]rune, 0)
    // Poping ")"
    for _, char := range(s){
        if char == ')'{
            if count == 0{
                continue
            } else {
                count -= 1
            }
        } else if char == '('{
            count += 1
        }
        popingLeft = append(popingLeft, char)
    }
    
    
    // Poping "(" if count >0 else return string(popingLeft)
    if count > 0{
        count = 0
        res := make([]rune, 0)
        for i := len(popingLeft) - 1; i > -1; i--{
            if popingLeft[i] == '('{
                if count == 0{
                    continue
                } else {
                    count -=1
                }
            } else if popingLeft[i] == ')'{
                count += 1
            }
            res = append(res, popingLeft[i])
        }
        // Reverse res
        for i, j := 0, len(res)-1; i < j; i, j = i+1, j-1 {
            res[i], res[j] = res[j], res[i]
        }
        return string(res)
    }else{
        
        return string(popingLeft)
    }
}
