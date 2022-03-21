func partitionLabels(s string) []int {
    // Init lastIdx to store every char's last index in s
    lastIdx := make(map[rune]int)
    for idx, char := range(s){
        lastIdx[char] = idx
    }
    // Init res, startIdx and endIdx
    res := make([]int, 0)
    startIdx, endIdx := 0, -1
    // Loops through s again
    for idx, char := range(s){
        // Update endIdx
        if lastIdx[char] >= endIdx{
            endIdx = lastIdx[char]
        }
        // If currIdx == endIdx, means we find a valid part
        // Move startIdx to next part's first index
        if idx == endIdx{
            res = append(res, endIdx - startIdx + 1)
            startIdx = endIdx + 1
        }
    }
    
    return res 
}
