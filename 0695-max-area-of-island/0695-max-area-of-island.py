class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        TC - O(R*C)
        SC - O(R*C) - for recursion
        '''
        area = 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        def helper(r,c):
            grid[r][c] = 0

            a = 1
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or grid[nr][nc] == 0:
                    continue
                
                
                a += helper(nr,nc)
            
            return a
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = max(area, helper(i,j))
        
        return area


