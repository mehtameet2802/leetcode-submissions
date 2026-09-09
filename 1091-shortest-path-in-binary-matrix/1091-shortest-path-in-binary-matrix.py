class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        '''
        What does one state represent? - its cell cost
        What does distance represent? - number of cells iterated from start to end
        Do all valid moves have the same cost? - yes
        When is a state marked visited? - as soon as the state is accessed is valid and helper function called on it, its marked visited
        How are valid next states generated? - the valid states must be within the limits of grid, have val 0 and be in either of the 8 directions
        Dangerous cases:
        - blocked start/end
        - one-cell grid
        - diagonal route
        Complexity:
        '''

        dirs = [[0,1],[1,0],[-1,0],[0,-1],[1,-1],[-1,1],[-1,-1],[1,1]]
        ROWS = len(grid)
        COLS = len(grid[0])
        queue = deque()

        if grid[0][0] == 1:
            return -1
            
        visited = set()

        visited.add((0,0))
        queue.append((0,0,1))
        while queue:

            (r,c, d) = queue.popleft()

            if r == ROWS-1 and c == COLS - 1:
                return d

            for dr,dc in dirs:
                nr = dr + r
                nc = dc + c

                if nr>=ROWS or nc>=COLS or nr<0 or nc<0 or (nr,nc) in visited or grid[nr][nc] != 0:
                    continue
                
                visited.add((nr,nc))
                queue.append((nr,nc,d+1))

        
        return -1
            



