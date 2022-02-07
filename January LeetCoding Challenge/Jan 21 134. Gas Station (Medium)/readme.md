

# Python 3 Solution Time: O(N) Space: O(1) 
## Naive Approach
Looping through gas and cost, each time set one be startStation and see if there exist a negative number in currentTank, then pass on next one
This takes O(n^2) 1. loop through gas 2. init startIdx and loop through rest of stations

## Naive Approach 
**THIS WILL CAUSE TLE DO NOT COPY THIS**
```
class Solution:
    # Naive Approach
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        
        for i in range(len(gas)):
            startIdx = i 
            currentGas = gas[startIdx] - cost[startIdx]
            startIdx = (startIdx + 1) % len(gas)
            while startIdx != i:
                if currentGas < 0:
                    break
                currentGas += (gas[startIdx] - cost[startIdx])
                startIdx = (startIdx + 1) % len(gas)
            if currentGas >= 0:
                return i    
        return -1
```
**THIS WILL CAUSE TLE DO NOT COPY THIS**

## Improvement Approach

In stead of looping gas twice, in this approach we loop it one pass. So we can make it O(N)
Now we add a new variable currentTank by checking if currentTank to be greater than 0 and totalTank is also greater than 0, then we found our answer.

> Step init: init totalTank, currentTank, startStation to be 0
> Loop(One pass)
> Step 1: Add up both totalTank and currentTank by (**gas[i]** - **cost[i]**)
> Step 2: Check if currentTank is less than 0
> Step 2.1 : If it is **less than** 0 it means that in currentTank's path we cant finish our route, so we set currentTank back to 0 and set startStation = **i + 1**
> Step 2.2 : If it greater or equal 0 we continue move on to next station see if we will run out of gas
> repeate 1 ~ 2 until loop all gas station
> Final : return startStation if totalTank >= 0 else -1 => Base case it that if totalTank is not greater or equal to 0, means that we can't find any route so return -1


## Complexity Analysis
* Time: O(n) : Let *n* be the length of the gas
* Space: O(1)

# [134. Gas Station](https://leetcode.com/problems/gas-station/)

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station. You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique

 

## Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
```
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.
```
## Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
```
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.
```
