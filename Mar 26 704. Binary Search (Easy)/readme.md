**[LeetCode Disscuss](https://leetcode.com/problems/binary-search/discuss/1885512/PythonGOC%2B%2B-Just-Binary-Search-Solution-and-Explanation)**
# [Python/GO/C++] 🌟 Just Binary Search Solution and Explanation 💕
## 1️⃣ Just Binary Search Approach:

**Algo**
1. Init left and right = 0, len(nums) - 1
2. while left <= right:
	* if nums[mid] == target => return mid
	* if nums[mid] < target => search right so we make left = mid + 1
	* if nums[mid] > target => search left so we make right = mid - 1
	
## Complexity Analysis
* Time: O(logN): Let N be length of nums.
* Space: O(1)

## Code

**Python**
```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
```
**Go**
```go
func search(nums []int, target int) int {
    left, right := 0, len(nums) - 1
    for left <= right{
        mid := (left + right) / 2
        if nums[mid] == target{
            return mid
        } else if nums[mid] < target{
            left = mid + 1
        } else{
            right = mid - 1
        }
    }
    return -1
    
}
```
**C++**
```cpp
class Solution {
public:
    int search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        
        while(left <= right){
            int mid = (left + right) / 2;
            if(nums[mid] == target) return mid;
            
            else if(nums[mid] < target) left = mid + 1;
            else right = mid - 1;
        }
        return -1;
    }
};
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
