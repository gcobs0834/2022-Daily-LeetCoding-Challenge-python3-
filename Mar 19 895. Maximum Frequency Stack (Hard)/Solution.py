class FreqStack:

    def __init__(self):
        self.freqStack = defaultdict(list)
        self.valFreq = defaultdict(int)
        self.maxFreq = 0

    def push(self, val: int) -> None:
        # Update valFreq
        self.valFreq[val] += 1
        currFreq = self.valFreq[val]
        # Update self.maxFreq
        self.maxFreq = max(self.maxFreq, currFreq)
        # Append val in currFreq slot
        self.freqStack[currFreq].append(val)
        
    def pop(self) -> int:
        # Get from maxFreq and last element in freqStack
        popValue = self.freqStack[self.maxFreq].pop()
        self.valFreq[popValue] -= 1
        #Update maxFreq
        if not self.freqStack[self.maxFreq]:
            self.maxFreq -= 1
        return popValue
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()
