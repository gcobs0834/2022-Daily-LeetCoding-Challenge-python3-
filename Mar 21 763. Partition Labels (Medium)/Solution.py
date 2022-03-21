class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        # Init lastIdx to store every char's last index in s
        lastIdx = {}
        for idx, char in enumerate(s):
            lastIdx[char] = idx
        # Init res, startIdx and endIdx
        res = []
        startIdx, endIdx = 0, -1
        # Loops through s again
        for idx, char in enumerate(s):
            # Update endIdx
            endIdx = max(lastIdx[char], endIdx)
            # If currIdx == endIdx, means we find a valid part
            # Move startIdx to next part's first index
            if idx == endIdx:
                res.append(endIdx - startIdx + 1)
                startIdx = endIdx + 1
        return res
