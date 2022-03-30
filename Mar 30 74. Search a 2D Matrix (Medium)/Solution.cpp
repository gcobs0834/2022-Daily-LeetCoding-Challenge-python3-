class Solution {
  public:
  bool searchMatrix(vector<vector<int>>& matrix, int target) {
    int M = matrix.size(), N = matrix[0].size();

    // binary search
    int low = 0, high = M*N - 1;
    while (low <= high){
        int mid = low + (high - low) / 2;
        int row = mid / N, col = mid % N;
        if (matrix[row][col] == target){
            return true;
        } else if (matrix[row][col] < target){
            low = mid + 1;
        }else{
            high = mid - 1;
        }
    }
    return false;
  }
};
