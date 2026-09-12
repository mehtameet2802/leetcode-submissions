class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        dirs = [[0,1],[1,0],[-1,0],[0,-1],[1,1],[-1,-1],[1,-1],[-1,1]]

        ROWS = len(grid)
        COLS = len(grid[0])

        if grid[0][0] == 1 or grid[ROWS-1][COLS-1]==1:
            return -1

        queue = deque([(0,0,1)])
        visited = set()
        visited.add((0,0))
        
        while queue:
            r,c,d = queue.popleft()

            if r == ROWS-1 and c == COLS-1:
                return d

            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                    continue

                if grid[nr][nc] == 1:
                    continue

                if (nr,nc) in visited:
                    continue
                
                visited.add((nr,nc))
                queue.append((nr,nc,d+1))
        
        return -1

