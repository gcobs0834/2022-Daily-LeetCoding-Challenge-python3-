# Two Pointer O(T) | O(1)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        s_pointer = 0
        for letter in t:
            if letter == s[s_pointer]:
                s_pointer += 1
            if s_pointer == len(s):
                return True
        return False

# HashMap O(T + S * logT) | O(T)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        # Creat a hashtable stores letter as key and all the letter index in value as list
        # Example abaa -> {"a" : [0, 2, 3], "b" : [1]}
        targetHash = defaultdict(list)
        for idx, letter in enumerate(t):
            targetHash[letter].append(idx)
            
        # Init t_idx = -1 which will represent currentLetter's index in t 
        t_idx = -1
        for letter in s:
            # Get target idxList, and find closest idx to t_idx
            letterIdxList = targetHash[letter]
            idxInHash = bisect.bisect_right(letterIdxList, t_idx) # This line will return index in letterIdxList not in t
            
            # If idx != len(letterIdxList) means there exist a letter after t_idx
            if idxInHash != len(letterIdxList):
                t_idx = letterIdxList[idxInHash] # Update t_idx
            else:
                # If we cant find a letter equals currentLetter return False
                return False
        # Once loop through all letter in s return True
        return True

# DP O(S * T) | O(S * T)
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not len(s):
            return True
        
        dp = [[0] * (len(s) + 1) for _ in range(len(t) + 1)]
        
        # Loops through dp
        for row in range(1, len(dp)):
            for col in range(1, len(dp[0])):
                sIdx, tIdx = col - 1, row - 1
                if s[sIdx] == t[tIdx]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])     
            # Early break, once we iterate through a row if dp[row][col] == len(s) means found a subsequence
            if dp[row][col] == len(s):
                return True   
        return False
        
        
