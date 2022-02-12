# O(M * N^2) | O(M * N)
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        return self.bfs(beginWord, endWord, wordList)
        
    def bfs(self, beginWord, endWord, wordList):
        visited = {}
        visited[beginWord] = True
        queue = deque([])
        self.appendInQueue(beginWord, 1, wordList, queue, visited)
        while queue:
            popWord, level = queue.popleft()
            visited[popWord] = True
            if popWord == endWord:
                return level
            self.appendInQueue(popWord, level, wordList, queue, visited)
        return 0
    
        
    def appendInQueue(self, word, level, wordList, queue, visited):
        for s in wordList:
            if s not in visited and self.checkOneLetter(word, s):
                queue.append((s, level + 1))
    
    def checkOneLetter(self, s1, s2):
        count = 0
        for c1, c2 in zip(s1, s2):
            if c1 != c2 :
                count +=1
            if count >1:
                return False
        return True

# O(M^2 * N) | O(M^2 * N) 
from collections import defaultdict
class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        wordHash = self.buildHash(wordList)
        
        return self.bfs(beginWord, endWord, wordHash)
        
    def bfs(self, beginWord, endWord, wordHash):
        visited = {}
        queue = deque([[beginWord, 1]]) # every element store [word, level]
        while queue:
            popWord, level = queue.popleft()
            visited[popWord] = True
            
            for i in range(len(popWord)):
                prefix = popWord[:i]
                suffix = popWord[i + 1:]
                key = prefix + '*' + suffix # key value
                # Traverse through and find next word to be append in queue
                for nextWord in wordHash[key]:
                    # End point
                    if nextWord == endWord:
                        return level + 1 
                    # Append next word in queue
                    if nextWord not in visited:
                        queue.append([nextWord, level + 1])
                # To prevent trverse same key again and find all visited
                wordHash[target] = [] 
        return 0
    
    
    def buildHash(self, wordList):
        wordHash = defaultdict(list)
        for word in wordList:
            # Put * in every possible index and add up its prefix and suffix
            for i in range(len(wordList[0])):
                prefix = word[:i]
                suffix = word[i + 1:]
                wordHash[prefix + '*' + suffix].append(word)
        return wordHash
