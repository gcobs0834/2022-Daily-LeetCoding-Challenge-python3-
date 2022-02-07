# Python 3 Solution Time: O(N^1.5) Space: O(N) 
## Recursive Solution
We can do recurrsive on each n and divide and conquer by making N down to N-1 ... ect. And we calculate value i by math.isqrt will sqrt n and floor it down.
> In Recursive Calls
> Step Init. if n == 0 means we lose the game, and if n in cache return,
> Step 1. calculate squareUpperBound by (math.isqrt(n))
> Step 2. Iterate from 1 to squareUpperBound and calculate newN = n - (i^2)
> Step 3. If ever found SquareGameHelper(newN, cache) = False => means we can win this in turn

## Complexity Analysis
* Time: O(N^1.5) : *N* is n. At most O(N^0.5) for each recursive call, and there are O(N) recursiverecursive calls in total.
* Space: O(N): There are O(N) recurrsive calls in total.

# [1510. Stone Game IV](https://leetcode.com/problems/stone-game-iv/)

Alice and Bob take turns playing a game, with Alice starting first.

Initially, there are n stones in a pile. On each player's turn, that player makes a move consisting of removing any non-zero square number of stones in the pile.

Also, if a player cannot make a move, he/she loses the game.

Given a positive integer n, return true if and only if Alice wins the game otherwise return false, assuming both players play optimally.

 

## Example 1:

Input: n = 1
Output: true
Explanation: Alice can remove 1 stone winning the game because Bob doesn't have any moves.
## Example 2:

Input: n = 2
Output: false
Explanation: Alice can only remove 1 stone, after that Bob removes the last one winning the game (2 -> 1 -> 0).
## Example 3:

Input: n = 4
Output: true
Explanation: n is already a perfect square, Alice can win with one move, removing 4 stones (4 -> 0).
 

Constraints:

1 <= n <= 105
