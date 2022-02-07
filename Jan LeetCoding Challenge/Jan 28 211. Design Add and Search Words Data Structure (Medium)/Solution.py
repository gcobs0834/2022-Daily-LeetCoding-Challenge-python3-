class WordDictionary:

    def __init__(self):
        self.trie = {}
        self.endSymbol = '*'
        

    def addWord(self, word: str) -> None:
        currentNode = self.trie
        for char in word:
            if char not in currentNode:
                currentNode[char] = {}
            currentNode = currentNode[char]
        currentNode[self.endSymbol] = True

    def search(self, word: str) -> bool:
        return self.searchHelper(0, word, self.trie)
    
    def searchHelper(self, idx, word, trie):
        for i in range(idx, len(word)):
            if word[i] == '.':
                for key in trie:
                    if key !=self.endSymbol and self.searchHelper(i + 1, word, trie[key]):
                        return True
                return False
            elif word[i] in trie:
                trie = trie[word[i]]
            else:
                return False
        return self.endSymbol in trie



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
