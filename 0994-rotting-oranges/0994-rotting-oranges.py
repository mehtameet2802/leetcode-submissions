class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        queue = deque([])
        perfect = 0
        empty = 0

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 2:
                    queue.append((i,j))
                elif grid[i][j] == 1:
                    perfect += 1
                else:
                    empty += 1
        
        if empty == ROWS*COLS:
            return 0
        
        ans = 0
        while queue:
            length = len(queue)

            for _ in range(length):
                r,c = queue.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]!=1:
                        continue
                    
                    grid[nr][nc] = 2
                    perfect -= 1
                    queue.append((nr,nc))
            
            ans += 1

        if perfect > 0:
            return -1
        
        return ans-1