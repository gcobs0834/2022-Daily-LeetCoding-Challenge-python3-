# [165. Compare Version Numbers](https://leetcode.com/problems/compare-version-numbers/)

Given two version numbers, version1 and version2, compare them.

Version numbers consist of one or more revisions joined by a dot '.'. Each revision consists of digits and may contain leading zeros. Every revision contains at least one character. Revisions are 0-indexed from left to right, with the leftmost revision being revision 0, the next revision being revision 1, and so on. For example 2.5.33 and 0.1 are valid version numbers.

To compare version numbers, compare their revisions in left-to-right order. Revisions are compared using their integer value ignoring any leading zeros. This means that revisions 1 and 001 are considered equal. If a version number does not specify a revision at an index, then treat the revision as 0. For example, version 1.0 is less than version 1.1 because their revision 0s are the same, but their revision 1s are 0 and 1 respectively, and 0 < 1.

Return the following:

If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 

## Example 1:

Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation: Ignoring leading zeroes, both "01" and "001" represent the same integer "1".
## Example 2:

Input: version1 = "1.0", version2 = "1.0.0"
Output: 0
Explanation: version1 does not specify revision 2, which means it is treated as "0".
## Example 3:

Input: version1 = "0.1", version2 = "1.1"
Output: -1
Explanation: version1's revision 0 is "0", while version2's revision 0 is "1". 0 < 1, so version1 < version2.
 

Constraints:

1 <= version1.length, version2.length <= 500
version1 and version2 only contain digits and '.'.
version1 and version2 are valid version numbers.
All the given revisions in version1 and version2 can be stored in a 32-bit integer.



# 🌟[Python 3] 2 Different Solutions and Explanation 💕

## 1️⃣ Split Approach:
> **Step 1.** Split version1 and version2 by "." and make it int(remove leading zeros) => O(M+N)
> **Step 2.** Iterate through v1 and v2, check which reversion is greater. Once we exceed a version's length while the other is not we check if the remaining version have not 0 value => O(max(M,N)

## Complexity Analysis
* Time: O(M + N) : Let M be length of version1 and N be length of version2.  O(M+N + max(M,N) => O(M+N)
* Space: O(M + N) : Extra space used for v1 and v2 

## Code
```
# O(M + N) | O(M + N)
class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Split both version1 and 2 by "."
        v1 = list(map(int, version1.split('.')))
        v2 = list(map(int, version2.split('.')))
        
        # Iterate throuth v1, v2 and compare the reversion
        for i in range(max(len(v1), len(v2))):
            i1 = v1[i] if i < len(v1) else 0 # If we exceed v1's length consider it 0
            i2 = v2[i] if i < len(v2) else 0 
            if i1 > i2:
                return 1
            elif i2 > i1:
                return -1
        return 0
```

## 2️⃣ Index Pointer Approach:
* In this approach, we simply iterate through both version chunk by chunk. Every chunk is a reversion before "." So that we can make compare these two reversion.

## Complexity Analysis
* Time: O(M + N) : Let M be length of version1 and N be length of version2.
* Space: O(M + N) : At worst **revision1 and revision2 equal to version1 and version2**. For example version1 = 12345, version2 = 77777, reversion1 = 012345, reversion2 = 077777

## Code
```
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
```
