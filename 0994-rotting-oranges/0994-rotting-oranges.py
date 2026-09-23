class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        good = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    good += 1
                elif grid[i][j] == 2:
                    queue.append((i,j))

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        if not queue:
            return -1 if good > 0 else 0 

        time = 0

        while queue:
            
            length = len(queue)
            for _ in range(length):
                r,c = queue.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                        continue
                    
                    if grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    good -= 1
                    queue.append((nr,nc))
            
            time += 1

        if good > 0:
            return -1
        
        return time-1
        
