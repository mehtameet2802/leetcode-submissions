class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dead = []
        live = []
        ROWS = len(board)
        COLS = len(board[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

        def helper(r,c):
            l = e = 0 
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                    continue

                if board[nr][nc] == 1:
                    l += 1
                else:
                    e += 1

            if board[r][c]:
                if l>3 or l<2:
                    return 0
                elif l==2 or l==3:
                    return 1
            else:
                if l == 3:
                    return 1
                return 0     
            
        for i in range(ROWS):
            for j in range(COLS):
                if helper(i,j):
                    live.append((i,j))
                else:
                    dead.append((i,j))
        

        for a,b in live:
            board[a][b] = 1
        
        for a,b in dead:
            board[a][b] = 0
