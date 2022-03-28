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
