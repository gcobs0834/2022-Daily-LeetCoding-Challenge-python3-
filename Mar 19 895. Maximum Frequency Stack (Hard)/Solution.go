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
