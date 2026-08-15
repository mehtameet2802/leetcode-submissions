class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        
        ROWS = len(grid)
        COLS = len(grid[0])

        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        ans = 0
        water = 0
        land = 0
        queue = deque([])

        for i in range(ROWS):
            for j in range(COLS):
                if grid[i][j] == 1:
                    land += 1
                    queue.append((i,j,0))
                    grid[i][j] = -1
                else:
                    water += 1

        if land == 0 or water == 0:
            return -1
        
        ans = 0
        while queue:

            length = len(queue)

            for _ in range(length):
                r,c,d = queue.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or grid[nr][nc] == -1:
                        continue
                    
                    nd = d + abs(nr-r) + abs(nc - c)
                    grid[nr][nc] = -1
                    ans = max(ans, nd)

                    queue.append((nr,nc,nd))
        
        return ans
            

