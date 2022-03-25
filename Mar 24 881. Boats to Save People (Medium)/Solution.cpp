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
