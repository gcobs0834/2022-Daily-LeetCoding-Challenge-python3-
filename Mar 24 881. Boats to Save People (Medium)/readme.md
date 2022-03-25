**[LeetCode Disscuss Post](https://leetcode.com/problems/boats-to-save-people/discuss/1878381/pythongoc-two-pointer-solution-and-explanations)**
# [Python/GO/C++] 🌟 Two Pointer Solution and Explanations 💕
## 1️⃣ Two Pointer Approach:
We can greedy sort the whole array. And set maximum weight of current people in the boat first. And then, we look for leftmost of people to find if there is a person whos weight can fit in same boat

**Algo**
1. Sort people ( O(nlogn) )
2. Loop through people from both left and right
	* Every time we set maximum weight in the boat (The rightmost of people) and check if there is a person can fit in same boat, so we look from leftmost.
	* Once found people[left] + people[right] <= limit. Means we can fit two people in same boat, We increase left by 1
## Complexity Analysis
* Time: O(NlogN): Let N be number of people. Since we sort people initially.
* Space: O(1)
## Dry Run

```
people = [2,49,10,7,11,41,47,2,22,6,13,12,33,18,10,26,2,6,50,10]
people.sort()
people = [2, 2, 2, 6, 6, 7, 10, 10, 10, 11, 12, 13, 18, 22, 26, 33, 41, 47, 49, 50]
EachBoats = [[50], [49], [47, 2], [41, 2], [33, 2], [26, 6], [22, 6], [18, 7], [13, 10], [12, 10], [11, 10]]
return 11
```


## Code

**Python**
```python
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # Sort people
        people.sort()
        # Init parameters
        res = 0
        left, right = 0, len(people) - 1
        # Two Pointer iteration
        while left <= right:
            # If we can fit two people in same boat
            if people[right] + people[left] <= limit:
                left += 1
            res += 1
            right -= 1
        return res
```
**Go**
```go
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
```
**C++**
```cpp
class Solution {
public:
    int numRescueBoats(vector<int>& people, int limit) {
        // Sort people
        sort(people.begin(), people.end());
        // Init parameters
        int left = 0, right = people.size() - 1;
        int res = 0;
        // Two Pointer iteration
        while(left <= right){
            // If we can fit two people in same boat
            if(people[left] + people[right] <= limit){
                left++;
            }
            res++;
            right--;
        }
        return res;
    }
};
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
