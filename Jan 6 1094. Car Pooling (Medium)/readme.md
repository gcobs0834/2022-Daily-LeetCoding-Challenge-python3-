# Python3 Solution 1

Time: O(T log(T)) or O(T log(n)) N depends on length of queue of destination on car
Space: O(N) for stored all destination in the trip

Note: I know best solution is O(N) based on maximum of 1000 stations. But this solution works on lesser trip and larger stations or not integer (If we use distance not  stations)

* Sort trip by _from in trips O(T log T) T = trips
* main loop takes O(T * log N) T = trips N depends on length of queue of destination on car

# Python3 Solution 2
Time: O(N) for stations in this case 1000
Space: O(N) for stations in this case 1000

Traverse trips and find out the number of the net increase passengers for each stop
from start station to end station, for each stop we calculate the number of passengers in the car.


# 1094. Car Pooling

There is a car with capacity empty seats. The vehicle only drives east (i.e., it cannot turn around and drive west).

You are given the integer capacity and an array trips where trip[i] = [numPassengersi, fromi, toi] indicates that the ith trip has numPassengersi passengers and the locations to pick them up and drop them off are fromi and toi respectively. The locations are given as the number of kilometers due east from the car's initial location.

Return true if it is possible to pick up and drop off all passengers for all the given trips, or false otherwise.

 

## Example 1:

Input: trips = [[2,1,5],[3,3,7]], capacity = 4
Output: false
## Example 2:

Input: trips = [[2,1,5],[3,3,7]], capacity = 5
Output: true
 

Constraints:

1 <= trips.length <= 1000
trips[i].length == 3
1 <= numPassengersi <= 100
0 <= fromi < toi <= 1000
1 <= capacity <= 105
