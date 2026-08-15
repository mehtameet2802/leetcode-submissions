class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        ROWS = len(maze)
        COLS = len(maze[0])

        queue = deque([(entrance[0],entrance[1])])

        ans = ROWS*COLS

        dirs = [[0,1],[1,0],[0,-1],[-1,0]]
        cur = 0
        while queue:

            length = len(queue)
            
            for _ in range(length):
                r,c = queue.popleft()

                # Current cell is an exit
                if (
                    (r, c) != (entrance[0], entrance[1])
                    and (
                        r == 0 or r == ROWS - 1 or
                        c == 0 or c == COLS - 1
                    )
                ):
                    return cur

                for dr, dc in dirs:
                    nr = r + dr
                    nc = c + dc

                    if nr<0 or nr>=ROWS or nc<0 or nc>=COLS:
                        continue

                    if maze[nr][nc] != ".":
                        continue

                    queue.append((nr,nc))
                    maze[nr][nc] = "+"
            cur += 1

        
        return -1
                




