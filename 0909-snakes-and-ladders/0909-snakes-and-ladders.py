class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        dice = "123456"
        ROWS = len(board)
        COLS = len(board[0])

        visited = {1}
        queue = deque([(1,0)])

        n = ROWS
        
        def get_pos(square):
            square -= 1

            r = n - 1 - square // n
            c = square % n

            if (n - 1 - r) % 2 == 1:
                c = n - 1 - c

            return r, c


        while queue:
            val,cnt = queue.popleft()

            if val == ROWS*COLS:
                return cnt

            for dice in range(1,7):
                nval = val + dice

                
                nr,nc = get_pos(nval)

                if nval > n*n:
                    continue

                if board[nr][nc] != -1:
                    nval = board[nr][nc]
                
                if nval in visited:
                    continue
                
                queue.append((nval,cnt+1))
                visited.add(nval)
        
        return -1
            
                
