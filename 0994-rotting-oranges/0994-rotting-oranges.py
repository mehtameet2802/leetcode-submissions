class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        '''
        Required output:
        What changes during one minute?
        What information must one state contain?
        Pattern prediction:
        Why this pattern fits:
        Initial state:
        Transition rule:
        When is a cell processed?
        Termination condition:
        Impossible-case condition:
        Invariant:
        Expected TC and SC:
        '''
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        time = 0
        good = 0
        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r,c))
                elif grid[r][c] == 1:
                    good += 1

        if good == 0:
            return time
        
        while queue:

            length = len(queue)

            for _ in range(length):

                r,c = queue.popleft()

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                        continue
                    
                    if grid[nr][nc] != 1:
                        continue
                    
                    grid[nr][nc] = 2
                    queue.append((nr,nc))
                    good -= 1
            
            time += 1
        

        if good > 0:
            return -1
        
        return time-1
