class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        ROWS = len(isWater)
        COLS = len(isWater[0])

        heights = [[0]*COLS for _ in range(ROWS)]
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]

        queue = deque([])
        visited = set()

        for i in range(ROWS):
            for j in range(COLS):
                if isWater[i][j] == 1:
                    queue.append((i,j))
                    visited.add((i,j))

        height = 1
        while queue:
            length = len(queue)

            for _ in range(length):
                r,c = queue.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or (nr,nc) in visited: 
                        continue
                    
                    heights[nr][nc] = height
                    visited.add((nr,nc))
                    queue.append((nr,nc))

            height += 1
        
        return heights

            