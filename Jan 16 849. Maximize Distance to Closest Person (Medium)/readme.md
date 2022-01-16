# Python 3 Solution Time: O(N) Space: O(1) 
## Main Idea
We update maxLen if we see a a person sitting in the ith by (idx - lastOneIdx) // 2, but be careful for the firstIdx and lastIdx it may differnt in this case
## Complexity Analysis
* Time: O(N) : N equals lenghth of seats
* Space: O(1) No other space used
