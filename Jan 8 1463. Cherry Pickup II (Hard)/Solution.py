class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.columns = len(grid[0])
        self.grid = grid
        
        @cache
        def dp(row, col1, col2):
            if col1 < 0 or col1 >= self.columns or col2 < 0 or col2 >= self.columns:
                return -1
            
            result = 0
            if col1 != col2:
                result  += self.grid[row][col1] + self.grid[row][col2]
            else:
                result += self.grid[row][col1]
            if row != self.rows - 1:
                result += max(dp(row + 1, nextCol1, nextCol2)
                             for nextCol1 in [col1 - 1, col1, col1 + 1]
                             for nextCol2 in [col2 - 1, col2, col2 + 1])
            return result
        
        return dp(0, 0, self.columns - 1)
        
class Solution2:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        self.rows = len(grid)
        self.columns = len(grid[0])
        
        dp = [[[-1]* self.columns for _ in range(self.columns)] for _ in range(self.rows)] # dp[row][col1][col2]
        
        for row in reversed(range(self.rows)):
            for col1 in range(self.columns):
                for col2 in range(self.columns):
                    result = 0
                    if col1 != col2:
                        result += grid[row][col1] + grid[row][col2]
                    else:
                        result += grid[row][col1]
                    if row != self.rows - 1:
                        result += self.nextRow(dp, row+1, col1, col2)
                    dp[row][col1][col2] = result
        return dp[0][0][self.columns - 1]
                    
    def nextRow(self, dp, row, col1, col2):
        currentMax = -1
        for newCol1 in [col1 - 1, col1, col1 + 1]:
            for newCol2 in [col2 - 1, col2, col2 + 1]:
                if 0 <= newCol1 < self.columns and 0 <= newCol2 < self.columns:
                    currentMax = max(currentMax , dp[row][newCol1][newCol2])
        return currentMax
