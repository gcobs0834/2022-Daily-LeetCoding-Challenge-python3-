// Two Pointer O(T) | O(1)
func isSubsequence(s string, t string) bool {
    if len(s) == 0{
        return true
    }
    S_rune, T_rune := []rune(s), []rune(t)
    s_length := len(s)
    s_pointer := 0
    
    for i := 0; i < len(T_rune); i++{
        if S_rune[s_pointer] == T_rune[i]{
            s_pointer += 1
        }
        if s_pointer == s_length{
            return true
        }
    }
    return false
}

// HashMap O(T + S * logT) | O(T)
func isSubsequence(s string, t string) bool {
    S_rune, T_rune := []rune(s), []rune(t)
     // Creat a hashtable stores letter as key and all the letter index in value as list
     // Example abaa -> {"a" : [0, 2, 3], "b" : [1]}
    targetHash := make(map[rune][]int)
    for i:=0; i < len(T_rune); i++{
        letter := T_rune[i]
        targetHash[letter] = append(targetHash[letter], i)
    }
    // Init t_idx = -1 which will represent currentLetter's index in t
    t_idx := -1
    
    for i:=0; i < len(S_rune); i++{
        // Get target idxList, and find closest idx to t_idx
        letter := S_rune[i]
        letterIdxList := targetHash[letter]
        // Linear search in letterIdxList find idx> t_idx
        foundMatch := false
        for _ , idx := range letterIdxList{
            if idx > t_idx{
                foundMatch = true
                t_idx = idx
                break
            } 
        }
        // if not found a match return false
        if !foundMatch{
            return false   
        }
    }
    return true
}
