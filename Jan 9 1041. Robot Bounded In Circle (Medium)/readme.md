# Python 3 Time: O(N) Space: O(1)
* **Main Idea**: A route to be a circle must have both **direction** and **coordinate** to be **North** and **(0,0)**
* Time: O(N) : Maximum do 4 times loop to back to north 4*N -> O(N)
* Space: O(1)
* We init east, south, west, north to be 0, 1, 2, 3. In this case if instruction is L: we substract (current - 1) and % 4 to get to correct direction. If instruction is R: do currentFace = (currentFace + 1) % 4 
* We build a function **move** to deal three instruction

# [1041. Robot Bounded In Circle](https://leetcode.com/problems/robot-bounded-in-circle/)


On an infinite plane, a robot initially stands at (0, 0) and faces north. The robot can receive one of three instructions:

"G": go straight 1 unit;
"L": turn 90 degrees to the left;
"R": turn 90 degrees to the right.
The robot performs the instructions given in order, and repeats them forever.

Return true if and only if there exists a circle in the plane such that the robot never leaves the circle.

 

## Example 1:

Input: instructions = "GGLLGG"
Output: true
Explanation: The robot moves from (0,0) to (0,2), turns 180 degrees, and then returns to (0,0).
When repeating these instructions, the robot remains in the circle of radius 2 centered at the origin.
## Example 2:

Input: instructions = "GG"
Output: false
Explanation: The robot moves north indefinitely.
## Example 3:

Input: instructions = "GL"
Output: true
Explanation: The robot moves from (0, 0) -> (0, 1) -> (-1, 1) -> (-1, 0) -> (0, 0) -> ...
 

Constraints:

1 <= instructions.length <= 100
instructions[i] is 'G', 'L' or, 'R'.
Accepted
149,331
Submissions
272,900
