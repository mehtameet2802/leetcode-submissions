class Solution:
    def findSafeWalk(self, grid: List[List[int]], health: int) -> bool:
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        dist = [[float('inf')]*COLS for _ in range(ROWS)]
        dist[0][0] = grid[0][0]

        queue = deque([(0,0)])

        while queue:
            r,c= queue.popleft()

            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                    continue
                
                new_cost = dist[r][c] + grid[nr][nc]

                if new_cost < dist[nr][nc]:
                    dist[nr][nc] = new_cost

                    if grid[nr][nc] == 0:
                        queue.appendleft((nr,nc))
                    else:
                        queue.append((nr,nc))
            
        return dist[ROWS-1][COLS-1] < health
        