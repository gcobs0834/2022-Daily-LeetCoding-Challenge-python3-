# Detailed Code Solution 1
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = " " + s +  " " #Since s does not contain any leading or trailing spaces.
        lastSpaceIdx = 0
        patternIdx = 0
        currentWord = ""
        patternMatch = defaultdict(int)
        wordMatch = defaultdict(int)
        for idx in range(1, len(s)):
            if patternIdx >= len(pattern): # In case pattern letters' number smaller than words
                return False
            
            currentPattern = pattern[patternIdx]
            if s[idx] == " ":
                if currentPattern not in patternMatch and currentWord not in wordMatch: #Build bijection map
                    patternMatch[currentPattern] = currentWord
                    wordMatch[currentWord] = currentPattern
                elif (patternMatch[currentPattern] != currentWord
                      or wordMatch[currentWord] != currentPattern): #Check if violate bijection
                    return False
                currentWord = ""
                lastSpaceIdx = idx
                patternIdx += 1
            else:
                currentWord += s[idx]
                
        return patternIdx == len(pattern) # In case pattern letters' number greater than words
      
# Pythonic Way Code Solution 2
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(" ")
        match = {}
        if len(words) != len(pattern): #Coner Case: check two sets have same number
            return False
        if len(set(words)) != len(set(pattern)): # In case ['abba'] ['cat cat cat cat'], for p have set of 2 and words have set of 1
            return False
        
        for i in range(len(words)):
            if pattern[i] not in match: # Init match if haven't seen this pattern
                match[pattern[i]] = words[i]
            elif match[pattern[i]] != words[i]: # If pattern match not equals to correspond word
                return False
        return True      
