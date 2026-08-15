class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:

        if grid[0][0] == 1:
            return -1
        
        queue = deque([(0,0)])

        dirs = [[0,1],[1,0],[-1,0],[0,-1],[-1,-1],[1,1],[1,-1],[-1,1]]

        ROWS = len(grid)
        COLS = len(grid[0])

        grid[0][0] = 1

        dist = 1

        while queue:
            length = len(queue)

            for _ in range(length):
                
                r,c = queue.popleft()

                if (r,c) == (ROWS-1, COLS-1):
                    return dist

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc]!=0:
                        continue
                    
                    queue.append((nr,nc))
                    grid[nr][nc] = 1

            dist += 1
        
        return -1