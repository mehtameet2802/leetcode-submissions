class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ROWS = len(mat)
        COLS = len(mat[0])

        dirs = [[0,1],[1,0],[0,-1],[-1,0]]

        queue = deque([])
        
        for i in range(ROWS):
            for j in range(COLS):
                if mat[i][j] == 0:
                    queue.append((i,j))

        dist = 0

        ans = [[0]*COLS for _ in range(ROWS)]

        while queue:
            length = len(queue)

            for _ in range(length):
                r,c = queue.popleft()

                for dr,dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS or mat[nr][nc] == 0:
                        continue

                    ans[nr][nc] = dist+1
                    queue.append((nr,nc))
                    mat[nr][nc] = 0
            dist += 1
        
        return ans

