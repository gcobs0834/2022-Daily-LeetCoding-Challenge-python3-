# Two pointer hashMap O(n1 + (n2 - n1) * 26 * n1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash = {}
        for s in s1:
            s1Hash[s] = s1Hash.get(s, 0) + 1
        startIdx = 0
        while startIdx <= len(s2) - len(s1):
            s1HashCopy = s1Hash.copy()
            count = 0
            for i in range(startIdx, startIdx + len(s1)):
                s = s2[i]
                if s in s1HashCopy and s1HashCopy[s] > 0:
                    s1HashCopy[s] -= 1
                    count += 1
                else:
                    break
            if count == len(s1):
                return True
            startIdx += 1
        return False

# Two pointer Array O(n1 + (n2 - n1) * 26 * n1)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Hash = [0] * 26
        for s in s1:
            idx = ord(s) - ord('a')
            s1Hash[idx] += 1
        
        startIdx = 0
        while startIdx <= len(s2) - len(s1):
            count = 0
            s1HashCopy = s1Hash[:]
            for i in range(startIdx, startIdx + len(s1)):
                idx = ord(s2[i]) - ord('a')
                if s1HashCopy[idx] > 0:
                    count += 1
                    s1HashCopy[idx] -= 1
                else:
                    break
            if count == len(s1):
                return True
            startIdx += 1
        return False

# Sliding Window Array O(n1 + 26 * (n2 - n1))
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Hash = [0] * 26
        
        for i in range(len(s1)):
            s1_idx = ord(s1[i]) - ord('a')
            s1Hash[s1_idx] += 1
            s2_idx = ord(s2[i]) - ord('a')
            s1Hash[s2_idx] -= 1
        left = 0
        
        for right in range(len(s1), len(s2)):
            if self.isMatch(s1Hash): return True
            leftCharIdx = ord(s2[left]) - ord('a')
            rightCharIdx = ord(s2[right]) - ord('a')
            s1Hash[leftCharIdx] += 1
            s1Hash[rightCharIdx] -= 1
            left += 1
            
        return self.isMatch(s1Hash)
    
    def isMatch(self, array):
        for i in array:
            if i != 0:
                return False
        return True
    
# Sliding Window Array Improved O(n1 + (n2 - n1))
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        s1Hash = [0] * 26
        
        for i in range(len(s1)):
            s1_idx = ord(s1[i]) - ord('a')
            s1Hash[s1_idx] += 1
            s2_idx = ord(s2[i]) - ord('a')
            s1Hash[s2_idx] -= 1
        left = 0
        match = self.countMatch(s1Hash)
        
        for right in range(len(s1), len(s2)):
            if match == 26: return True
            
            leftCharIdx = ord(s2[left]) - ord('a')
            rightCharIdx = ord(s2[right]) - ord('a')
            
            if s1Hash[leftCharIdx] == 0:
                match -= 1
            s1Hash[leftCharIdx] += 1
            if s1Hash[leftCharIdx] == 0:
                match += 1

            if s1Hash[rightCharIdx] == 0:
                match -= 1    
            s1Hash[rightCharIdx] -= 1
            if s1Hash[rightCharIdx] == 0:
                match += 1
                
            left += 1
            
        return match == 26
    
    def countMatch(self, array):
        count = 0
        for i in array:
            count += 1 if i == 0 else 0
        return count
