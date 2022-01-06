class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        fromSortedList = sorted(trips, key = lambda x: x[1])
        inCarNum = 0
        dest = [] # sorted queue
        destHash = {} # Store seen currentPassengers' destination and get off numbers
        
        def BS_Insert(num, low, high, array, mid = 0): # O(log n) Modified Binary Search for idx to insert
            if low > high:
                if num < array[mid]:
                    array.insert(mid, num)
                else:
                    array.insert(mid + 1, num)
                return
            mid = (low + high) // 2
            if num > array[mid]:
                mid = BS_Insert(num, (mid + 1), high, array, mid)
            elif num < array[mid]:
                mid = BS_Insert(num, low, (mid - 1), array, mid)
            else:
                return  # if already in dest just return 
        
        def pushInHash(destHash, to, num): # push Num of passengers in certain destination
            if to in destHash:
                destHash[to] += num
            else:
                destHash[to] = num
        
        for trip in fromSortedList: # O(N) N = trips
            num, _from, _to = trip

            while len(dest) and _from >= dest[0]: # Pop out number of passengers who reached destination
                inCarNum -= destHash[dest.pop(0)]
                         
            if num + inCarNum > capacity: # Once the number of passengers in the car exceeds the capacity return False
                return False
            inCarNum += num 
                             
            if not len(dest): # Do binary search to insert in sorted list takes O(log n) n = length of stations
                dest.append(_to)
            elif _to > dest[-1]:
                dest.append(_to)
            else:
                BS_Insert(_to, 0, len(dest) - 1, dest)
                
            pushInHash(destHash, _to, num)
            
        return True

        
    
class Solution2(object):
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        in_car, increase = 0, [0] * 1001
        for [n, fro, to] in trips:
            increase[fro] += n
            increase[to] -= n
        for i in range(0, 1001):
            in_car += increase[i]
            if in_car > capacity: return False
        return True
        
