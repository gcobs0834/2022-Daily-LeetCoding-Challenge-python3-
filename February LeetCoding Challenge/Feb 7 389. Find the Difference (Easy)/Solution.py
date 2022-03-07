# HashMap O(N) | O(N)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        stringHash = {}
        
        for char in s:
            stringHash[char] = stringHash.get(char, 0) + 1
            
        for char in t:
            stringHash[char] = stringHash.get(char, 0) - 1
            if stringHash[char] == -1:
                return char
            
# XOR Operation O(N) | O(1)    
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        
        for char in s:
            res ^= ord(char)
        for char in t:
            res ^= ord(char)
        return chr(res)
