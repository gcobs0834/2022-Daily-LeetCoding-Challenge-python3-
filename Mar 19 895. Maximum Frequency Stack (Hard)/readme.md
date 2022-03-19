**[LeetCode Discuss Post](https://leetcode.com/problems/maximum-frequency-stack/discuss/1862020/pythongo-two-hashmap-solution-and-explanation)**
# [Python/GO] 🌟 Two HashMap Solution and Explanation 💕
## 1️⃣ Main Idea:
In this approach, we init two different hashmap and a var call maxFreq = 0.
1. freqStack : key would be frequency and value be a stack for that frequency
2. valFreq: whichs key is val, and its value would be the val's frequency in FreqStack.

**Push**
1. Update valFreq = > self.valFreq[val] += 1
2. Update maxFreq = > if currFreq > maxFreq, update it
3. Append current value in freqStack[currFreq]

**Pop**
1. Pop the value from freqStack[maxFreq] which guarantee that we will pop the **last element from maxFreq**
2. Decrease valFreq[popValue] by 1
3. Update maxFreq if freqStack[maxFreq] is empty. Means we have to move maxFreq decrease by 1 to find new maxFreq
4. return PopVALUE

## Complexity Analysis
* Time: O(1): Both push and pop are constant time
* Space: O(N): Let N be number of element in freqStack

## Code

**Python**
```python
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
```
**Go**
```go
// Init struct and Constructor
type FreqStack struct {
    freqStack map[int][]int
    valFreq map[int]int
    maxFreq int
}

func Constructor() FreqStack {
    return FreqStack{
		freqStack: make(map[int][]int),
		valFreq:   make(map[int]int),
        maxFreq: 0,
	}
}


func (this *FreqStack) Push(val int)  {
    // Update valFreq
    this.valFreq[val]++
    // Update maxFreq
    currFreq := this.valFreq[val]
    if currFreq > this.maxFreq{
        this.maxFreq = currFreq
    }
    // Append val in freqStack[currFreq]
    this.freqStack[currFreq] = append(this.freqStack[currFreq], val)
}


func (this *FreqStack) Pop() int {
    // Get from maxFreq and last element in freqStack
    lenOfMaxFreq := len(this.freqStack[this.maxFreq])
    popValue := this.freqStack[this.maxFreq][lenOfMaxFreq - 1]
    this.freqStack[this.maxFreq] = this.freqStack[this.maxFreq][:lenOfMaxFreq - 1]
    // Update valFreq
    this.valFreq[popValue]--
    // Update maxFreq
    if len(this.freqStack[this.maxFreq]) == 0{
        this.maxFreq--
    }
    return popValue
}

```
* See more 2022 Daily Challenge Solution : [GitHub](https://github.com/gcobs0834/2022-Daily-LeetCoding-Challenge-python3-)
