# O(N) | O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        nonValidIdx = set()
        # Find invalid ")" store in nonValidIdx
        for idx, char in enumerate(s):
            if char == "(":
                stack.append(idx)
            elif char == ")":
                if stack:
                    stack.pop()
                else:
                    nonValidIdx.add(idx)
        # If stack != empty, remaining "(" is nonValidIdx
        for idx in stack:
            nonValidIdx.add(idx)
            
        # Create result list
        res = []
        for idx, char in enumerate(s):
            if idx not in nonValidIdx:
                res.append(char)
                
        return "".join(res)

# O(N) | O(N)
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        count = 0
        res = []
        # Poping ")"
        for char in s:
            if char == ")":
                if count > 0:
                    count -= 1
                else:
                    continue
            elif char == "(":
                count += 1
            res.append(char)
        # Popping "(" if count > 0
        if count > 0:
            count = 0
            for i in range(len(res))[::-1]:
                if res[i] == "(":
                    if count > 0:
                        count -= 1
                    else:
                        res[i] = ""
                elif res[i] == ")":
                    count += 1
                    
        return "".join(res)       
