class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        self.EAST, self.SOUTH, self.WEST, self.NORTH = 0, 1, 2, 3 # If R: currentFace = (currentFace + 1) % 4 / L:currentFace = (currentFace - 1) % 4
        self.currentFace = self.NORTH
        self.currentCoordinate = [0, 0]
        turned = True
        
        while True:
            for instr in instructions:
                self.move(instr) # To deal with instructions
                
            if self.currentFace == self.NORTH:
                break
                
        return self.currentCoordinate == [0,0]
                
                
                
    def move(self, instruction):
        if instruction == 'G':
            if self.currentFace == self.NORTH:
                self.currentCoordinate[1] +=1
            elif self.currentFace == self.EAST:
                self.currentCoordinate[0] += 1
            elif self.currentFace == self.SOUTH:
                self.currentCoordinate[1] -= 1
            elif self.currentFace == self.WEST:
                self.currentCoordinate[0] -= 1
        elif instruction == 'L':
            self.currentFace = (self.currentFace - 1) % 4
        elif instruction == 'R':
            self.currentFace = (self.currentFace + 1) % 4
