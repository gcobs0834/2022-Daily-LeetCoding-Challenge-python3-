class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        def isSameCase(l, r, word, isUpper):
            while l <= r:
                if word[l].isupper() != isUpper or word[r].isupper() != isUpper:
                    return False
                l += 1
                r -= 1
            return True
        
        if len(word) == 1: # Base Case
            return True
        
        if word[0].isupper() and word[1].isupper(): #Case 1 "USA"
            return isSameCase(1, len(word) - 1, word, True)
        elif word[0].islower() and word[1].islower(): #Case 2 "leetcode"
            return isSameCase(1, len(word) - 1, word, False)
        elif word[0].isupper() and word[1].islower(): # Case 3 "Google"
            return isSameCase(1, len(word) - 1, word, False)
        else:
            return False
        
