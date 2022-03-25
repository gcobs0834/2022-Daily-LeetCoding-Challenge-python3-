func numRescueBoats(people []int, limit int) int {
    // Sort people
    sort.Ints(people)
    // Init parameters
    left, right := 0, len(people) - 1
    res := 0
    // Two Pointer iteration
    for left <= right{
        // If we can fit two people in same boat
        if people[left] + people[right] <= limit{
            left += 1
        }
        res += 1
        right -= 1
    }
    return res
}
