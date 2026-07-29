class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])

        visited = set()

        cnt = 0
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]

        def helper(r,c):

            visited.add((r,c))

            for dr, dc in dirs:
                nr = r+dr
                nc = c+dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in visited or grid[nr][nc]=="0":
                    continue
                
                helper(nr,nc)

        
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1" and (r,c) not in visited:
                    helper(r,c)
                    cnt+=1
        
        return cnt
