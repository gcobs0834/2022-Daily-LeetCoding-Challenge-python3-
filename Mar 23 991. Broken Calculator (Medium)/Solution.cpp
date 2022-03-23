// Recursive
class Solution {
public:
    int brokenCalc(int startValue, int target) {
        // Once target <= startValue, we only do subtract 1 to fit the target
        if (target <= startValue){
            return startValue - target;
        }
        // Base Condition
        if (target % 2 == 0){
            return 1 + brokenCalc(startValue, target / 2);
        } else{
            return 1 + brokenCalc(startValue, target + 1);
        }
    }
};

// Iterative
class Solution {
public:
    int brokenCalc(int startValue, int target) {
        int steps = 0;
        // Base Condition
        while (target > startValue){
            steps++;
            if (target % 2 == 0){
                target /= 2;
            } else{
                target++;
            }
        }
        // Once target <= startValue, we only do subtract 1 to fit the target
        return steps + startValue - target;
    }
};
