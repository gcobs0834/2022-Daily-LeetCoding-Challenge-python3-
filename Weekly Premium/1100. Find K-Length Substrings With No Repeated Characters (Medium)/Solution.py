# SLiding Window
class Solution:
    def numKLenSubstrNoRepeats(self, s: str, k: int) -> int:
        letterHash = {}
        res = 0
        l = 0
        for r in range(len(s)):
            # If length of window > k, increase left pointer and delete key s[l]
            if r - l + 1 > k:
                del letterHash[s[l]]
                l += 1
            
            # Move left to non repeated character
            if s[r] in letterHash:
                lastIdx = letterHash[s[r]]
                while l <= lastIdx:
                    del letterHash[s[l]]
                    l += 1
            # Add right pointer in current letterHash
            letterHash[s[r]] = r
            # Once equals k, res += 1
            if r - l + 1 == k:
                res += 1
        return res
