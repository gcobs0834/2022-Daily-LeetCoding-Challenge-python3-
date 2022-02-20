
# 🌟[Python 3] Greedy Sort Solution and Explanation

## 1️⃣ Greedy Naive Approach:
* Step 1. Sort intervals by first index
* Setp 2. Compare with current interval and last interval, so we can check whether current interval and last interval overlaps and covered by intervals[i][1] <= lastInterval[1].
> **(Edge Case)** : Since we compare two intervals ending point, once current interval's ending point is **smaller** than last interval's, in most of time it works.
> But there is a edge case that these two interval's starting point are equal. So we could add another **if statement** to update last interval to a larger interval
## Dry run
Intervals = [[1,4],[3,6],[2,8],[1,5],[2,3]]
```
#sorted
[[1, 4], [1, 5], [2, 8], [2, 3], [3, 6]]
# [1,4] and [1,5] is one of our edge cases
Init => count = 1, lastInterval = [1, 4]
# In for loop
i = 1 => count = 1, lastInterval = [1, 5] #Edge case swap lastInterval
i = 2 => count = 2, lastInterval = [2, 8]
i = 3 => count = 2, lastInterval = [2, 8] # [2, 3]'s ending point is smaller than [2, 8]
i = 4 => count = 2, lastInterval = [2, 8] # [3, 6]'s ending point is smaller than [2, 8]

Final => return 2
```

## Complexity Analysis
* Time: O(Nlog(N)) : Let N be length of intervals
* Space: O(N) :  Sorting in Python


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/294e3e8ded8601a3ee93957873916f525d69e63b/Feb%2020%201288.%20Remove%20Covered%20Intervals%20(Medium)/Solution.py#L2)

## 2️⃣ Greedy Improved Approach:

**In order two deal with the edge case this time we sort intervals not only by first index of interval and both second index with large number first**
* Step 1. Sort intervals by first index (Smaller first index, and larger second index)
* Setp 2. Compare with current interval and last interval, so we can check whether current interval and last interval overlaps and covered by intervals[i][1] <= lastInterval[1].
## Exapmle

```
intervals.sort(key = lambda x: x[0])
> [[1, 4], [1, 5], [2, 8], [2, 3], [3, 6]]

intervals.sort(key = lambda x: (x[0], -x[1]))
> [[1, 5], [1, 4], [2, 8], [2, 3], [3, 6]]
```

## Complexity Analysis
* Time: O(Nlog(N)) : Let N be length of intervals
* Space: O(N) :  Sorting in Python


## Code
See [Solution.py](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-/blob/294e3e8ded8601a3ee93957873916f525d69e63b/Feb%2020%201288.%20Remove%20Covered%20Intervals%20(Medium)/Solution.py#L20)

# [1288. Remove Covered Intervals](https://leetcode.com/problems/remove-covered-intervals/)

Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list.

The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.

Return the number of remaining intervals.

 

## Example 1:

Input: intervals = [[1,4],[3,6],[2,8]]
Output: 2
Explanation: Interval [3,6] is covered by [2,8], therefore it is removed.
## Example 2:

Input: intervals = [[1,4],[2,3]]
Output: 1
 

Constraints:

1 <= intervals.length <= 1000
intervals[i].length == 2
0 <= li <= ri <= 105
All the given intervals are unique.
