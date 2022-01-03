class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        trustList = [0] * (n+1) # ignore index 0, since we have 1 ~ n person for each index
        currentJudge = 1 # For index n person
        trustHash = {}
        
        for pair in trust:
            if pair[0] not in trustHash:
                trustHash[pair[0]] = True # indicate that person n trust someone
            trustList[pair[1]] += 1 # count if the currentJudge be trusted by everyone
            if trustList[pair[1]] > trustList[currentJudge]: # update the Judge by who got most trust
                currentJudge = pair[1]
        if trustList[currentJudge] == n - 1 and currentJudge not in trustHash:
            return currentJudge
        
        return -1
