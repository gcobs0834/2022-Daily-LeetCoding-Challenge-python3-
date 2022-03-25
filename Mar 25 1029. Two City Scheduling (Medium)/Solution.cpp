class Solution {
public:
    int twoCitySchedCost(vector<vector<int>>& costs) {
        // Sort by diff
        sort(costs.begin(),
             costs.end(),
             [](const vector<int>&a, const vector<int>&b) { return a[0] - a[1] < b[0] - b[1];});
        
        // Add res from both leftmost aCosts and rightmost bCosts
        int res = 0, N = costs.size()/2;
        for(int i = 0; i < N; i++){
            res += costs[i][0] + costs[i + N][1];
        }
        return res;
    }
};
