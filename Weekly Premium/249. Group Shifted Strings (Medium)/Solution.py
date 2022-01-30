class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        
        distHash = defaultdict(list)
        
        for s in strings:
            if len(s) == 1:
                distHash['0'].append(s)
                continue
            distList = []
            for i in range(1, len(s)):
                dist = (ord(s[i - 1]) - ord(s[i])) % 26
                distList.append(dist)
                
            distString = self.listToString(distList)
            distHash[distString].append(s)
            
        res = []
        
        for key in distHash.keys():
            res.append(distHash[key])
        return res
        
    def listToString(self, array):
        res = ""
        for num in array:
            res += str(num) + ':'
        return res
                    
