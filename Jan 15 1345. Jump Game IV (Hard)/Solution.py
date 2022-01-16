class Solution:
    def minJumps(self, arr):
        if len(arr) == 1:
            return 0
        
        graph = defaultdict(list)
        
        for idx, num in enumerate(arr):
            graph[num].append(idx) # store every idx that can jump from number
        
        distance = [float('inf')] * len(arr) # distance from idx 0

        visited, visitedNum = set(), set() # init visited matrix, and visitedNum in line 29 do mutiple times
        queue = deque([(0, 0)])
        step = 0
        
        while queue: #BFS queue
            idx, currentStep = queue.popleft()
            if idx == len(arr) - 1: return currentStep
            num = arr[idx]
            distance[idx] = currentStep
            
            if idx - 1 >= 0 and idx - 1 not in visited: # add left index to queue
                visited.add(idx)
                queue.append((idx - 1, currentStep + 1))
            if idx + 1 < len(arr) and idx + 1 not in visited: # add right index to queue
                visited.add(idx)
                queue.append((idx + 1, currentStep + 1))
            if num not in visitedNum: # check if same num been add in visitedNum otherwise nextline for loop would do mutiple times
                for i in graph[num]: # add same num index to queue
                    if i not in visited:
                        visited.add(idx)
                        queue.append((i, currentStep + 1))
            visitedNum.add(num)
            
                        
