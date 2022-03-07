# HashMap
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        pHash = defaultdict(int)
        count = 0
        for char in p:
            pHash[char] += 1
        res = []
        rHash = defaultdict(int)
        
        for idx, char in enumerate(s):
            if idx >= len(p): # Deleting last idx to maintain sliding window
                letterToRemove = s[idx - len(p)]
                if rHash[letterToRemove] > 1:
                    rHash[letterToRemove] -= 1
                else:
                    del rHash[letterToRemove]
            rHash[char] += 1
            if pHash == rHash:
                res.append(idx - len(p) + 1) 
        return res

# Array Index Map
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        sHash, pHash = [0] * 26, [0] * 26
        
        for char in p:
            idx = ord(char) - ord('a')
            pHash[idx] += 1
        
        res = []
        for i, char in enumerate(s):
            if i >= len(p):
                removeIdx = ord(s[i - len(p)]) - ord('a')
                sHash[removeIdx] -= 1
            charIdx = ord(char) - ord('a')
            sHash[charIdx] += 1
            
            if sHash == pHash:
                res.append(i - len(p) + 1)
        
        return res   
