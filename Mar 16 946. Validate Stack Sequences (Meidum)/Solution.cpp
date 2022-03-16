// Two Pointer O(N) | O(N)
class Solution {
public:
    bool validateStackSequences(vector<int>& pushed, vector<int>& popped) {
        // Init two pointer and stack
        stack<int> Stack;
        int pushIdx = 0 , popIdx = 0;
        // Iterate through pushed   
        while (pushIdx < pushed.size() && popIdx < popped.size()){
            Stack.push(pushed[pushIdx]);
            pushIdx++;
            // Once current top == popped[idx], we start pop it and move popIdx forward
            while (!Stack.empty() && Stack.top() == popped[popIdx]){
                Stack.pop();
                popIdx++;
            }
        }
        // If stack is not empty means we cannot find a sequence
        return Stack.empty();
    }
};
