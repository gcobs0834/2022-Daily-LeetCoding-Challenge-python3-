class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        fromSortedList = sorted(trips, key = lambda x: x[1])
        inCarNum = 0
        dest = []
        destHash = {}
        
        def BS_Idx(num, low, high, array, mid = 0):
            if low > high:
                return mid if num < array[mid] else mid + 1
            mid = (low + high) // 2
            if num > array[mid]:
                mid = BS_Idx(num, (mid + 1), high, array, mid)
            elif num < array[mid]:
                mid = BS_Idx(num, low, (mid - 1), array, mid)
            else:
                return None
            return mid
        
        def putInHash(destHash, to, num):
            if to in destHash:
                destHash[to] += num
            else:
                destHash[to] = num
        
        for trip in fromSortedList:
            num, _from, _to = trip

            while len(dest) and _from >= dest[0]:
                inCarNum -= destHash[dest[0]]
                dest.pop(0)
                
            if num + inCarNum > capacity:
                return False
            inCarNum += num 
                             
            if not len(dest):
                dest.append(_to)
            elif _to > dest[-1]:
                dest.append(_to)
            else:
                _idx = BS_Idx(_to, 0, len(dest) - 1, dest)
                if _idx is not None:
                    dest.insert(_idx, _to)
            putInHash(destHash, _to, num)
            
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
        
