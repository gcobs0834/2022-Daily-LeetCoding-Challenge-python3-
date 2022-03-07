# O(M + N) | O(M + N)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split both version1 and 2 by "."
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        # Iterate throuth v1, v2 and compare the reversion
        for i in range(max(len(v1), len(v2))):
            i1 = v1[i] if i < len(v1) else 0
            i2 = v2[i] if i < len(v2) else 0 
            if i1 > i2:
                return 1
            elif i2 > i1:
                return -1
        return 0
            
            
# O(M + N) | O(M + N)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        v1Idx, v2Idx = 0, 0
        
        while v1Idx < len(version1) or v2Idx < len(version2):
            # Set both reversion init to 0, so that if they exceed its length we can consider it 0
            revision1, revision2 = "0", "0"
            # Iterate through version1 and version2 to check current revision
            while v1Idx < len(version1) and version1[v1Idx] != ".":
                revision1 += version1[v1Idx]
                v1Idx += 1
            while v2Idx < len(version2) and version2[v2Idx] != ".":
                revision2 += version2[v2Idx]
                v2Idx += 1
                
            if int(revision1) > int(revision2):
                return 1
            elif int(revision2) > int(revision1):
                return - 1
            # Once they equal each other, we than check next block of revision
            v1Idx += 1
            v2Idx += 1
            
        return 0
