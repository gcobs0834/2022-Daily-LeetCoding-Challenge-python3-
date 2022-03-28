**[LeetCode Discuss Post](https://leetcode.com/problems/search-in-rotated-sorted-array-ii/discuss/1891748/pythongoc-binary-search-and-linear-forward-solution-and-explanation)**
# [Python/GO/C++] 🌟Binary Search and Linear forward Solution and Explanation 💕
## 1️⃣ Main Idea:
At **[33. Search in Rotated Sorted Array](https://leetcode.com/problems/search-in-rotated-sorted-array/)**, when we try to use binary search in the rotated array. 
We need to consider if we are in the left sorted array or right sorted array, but but nums may contain duplicates.
For example```nums = [1,1,1,1,1,1,1,1,1,13,1,1,1,1,1,1,1,1,1,1,1,1]``` We can't not actually tell whether current mid is in left sorted arr or right sorted array.
So we can't use binary search in this situation, we just linearly search increse left++ to find target value.
**Algo**
In the search section there are 4 different condition:
1. If nums[mid] == target => Return True
2. If nums[left] < nums[mid] : **nums[mid] is at left sorted arr**
	* If nums[left] > target or nums[mid] < target: **Search Right, left = mid + 1**
	* Else: **Search Left, right = mid - 1**
3. If nums[left] > nums[mid] : **nums[mid] is at right sorted arr**
	* If nums[right] < target or nums[mid] > target: **Search left, right = mid - 1**
	* Else: **Search Right, left = mid + 1**
4. If none of above, means we don't know if we are at left or right part => **Linear Search**
5. **Final** If can't find num return False

## Complexity Analysis
* Time: Worst: O(N), Best: O(logN): Let N be length of nums.
* Space: O(1)

## Code

**Python**
```python
class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True
            # We're in left sorted arr
            elif nums[left] < nums[mid]:
                if nums[left] > target or nums[mid] < target:
                    # Search right
                    left = mid + 1
                else:
                    # Search left
                    right = mid - 1
            # We're in right sorted arr
            elif nums[left] > nums[mid]:
                if nums[right] < target or nums[mid] > target:
                    # Search left
                    right = mid - 1
                else:
                    # Search right
                    left = mid + 1
            # Can't decide go left or right, just dummy add 1
            else:
                left += 1
        return False
```
**Go**
```go
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

```
**C++**
```cpp
class Solution {
public:
    bool search(vector<int>& nums, int target) {
        int left = 0, right = nums.size() - 1;
        while (left <= right){
            int mid = (left + right) / 2;
            if (nums[mid] == target){
                return true;
            } else if (nums[left] < nums[mid]){ // We're in left sorted arr
                if (nums[left] > target || nums[mid] < target){
                    // Search right
                    left = mid + 1;
                } else{
                    // Search left
                    right = mid - 1;
                }
            } else if (nums[left] > nums[mid]){ // We're in right sorted arr
                if (nums[right] < target || nums[mid] > target){
                    // Search left
                    right = mid - 1;
                }else{
                    // Search right
                    left = mid + 1;
                }
            } else{ // Can't decide go left or right, just dummy add 1
                left++;
            }
        }
        return false;
    }
};
```

* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
