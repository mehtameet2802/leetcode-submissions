class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        area = 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        def helper(r,c):
            visited.add((r,c))

            a = 1
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or (nr,nc) in visited or grid[nr][nc] == 0:
                    continue
                
                a += helper(nr,nc)
            
            return a
        
        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    area = max(area, helper(i,j))
        
        return area


