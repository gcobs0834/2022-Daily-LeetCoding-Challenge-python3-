# O(n log(n)) Since we sorted in final step
class Solution1:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        
        def findSequential(low, high, startNum, res):
            strNum = str(startNum)
            addDigit = int(strNum[-1]) + 1
            newNum = int(strNum + str(addDigit))
            if newNum > high:
                return
            elif newNum >= low:
                res.append(newNum)
            if addDigit == 9:
                return
            else:
                findSequential(low, high, newNum, res)
        res = []
        for i in range(1,9):
            findSequential(low, high, i, res)
            
        return sorted(res)

# O(n) Better
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        sequential = "123456789"
        lowerBound = len(str(low))
        upperBound = len(str(high))
        res = []
        for length in range(lowerBound, upperBound + 1):
            for i in range(0, 10 - length):
                currentNum = int(sequential[i: i+length])
                if low <= currentNum <= high:
                    res.append(currentNum)
        return res
