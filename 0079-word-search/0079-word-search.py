class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def helper(r,c,i):
            if i == len(word):
                return True
            
            for dr, dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nr>=ROWS or nc<0 or nc>=COLS or board[nr][nc] != word[i] or (nr,nc) in visited:
                    continue
                
                visited.add((nr,nc))

                if helper(nr,nc, i+1):
                    return True
                
                visited.remove((nr,nc))
            
            return False
        

        for i in range(ROWS):
            for j in range(COLS):
                if board[i][j] == word[0]:
                    visited.add((i,j))
                    if helper(i,j,1):
                        return True
                    visited.remove((i,j))
        
        return False


