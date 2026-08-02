class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        '''
        Pattern - Matrix Iteration - Directions

        TC - O(R*C)
        SC - O(1)
        '''

        dead = []
        live = []
        ROWS = len(board)
        COLS = len(board[0])

        dirs = [[0,1],[0,-1],[1,0],[-1,0],[1,1],[-1,-1],[1,-1],[-1,1]]

        # | Value | Meaning     |
        # | ----- | ----------- |
        # | 0     | dead → dead |
        # | 1     | live → live |
        # | 2     | live → dead |
        # | 3     | dead → live |


        def helper(r,c):
            l = 0 
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                    continue

                if board[nr][nc] == 1 or board[nr][nc] == 2:
                    l += 1

            if board[r][c]:
                if l>3 or l<2:
                    return 2
                elif l==2 or l==3:
                    return 1
            else:
                if l == 3:
                    return 3
                return 0     
            
        for i in range(ROWS):
            for j in range(COLS):
                board[i][j] = helper(i,j)
        
        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == 3:
                    board[i][j] = 1
                elif board[i][j] == 2:
                    board[i][j] = 0 
