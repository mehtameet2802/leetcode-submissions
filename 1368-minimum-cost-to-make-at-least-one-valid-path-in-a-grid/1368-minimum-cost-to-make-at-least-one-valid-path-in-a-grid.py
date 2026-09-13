class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        '''
        Required output: - min cost to go from start to target

        What does one state represent? - direction we can go

        From one cell, what moves are available? - go in the fiven direction, change to right, change to down

        What is the cost of each possible move? - same direction 0, if changing to right or down 1

        Can reaching the same cell again ever be useful?

        Pattern prediction: 0-1 BFS or Djikstar - taking 0-1 BFS for now

        Data structures: queue

        Distance/visited rule: I am unbale to recollect but I think in 0-1 BFS visited is not maintained, we insert in front of queue if cost is 0 else in end of queue if cost is 1.
        NO I think we will beed to maintain a distance 2d matrix, when ever a state is take from queue we check if the new dist is less than the existing dist then we update else ke skip the state

        Invariant:

        Expected TC and SC:

        Dangerous cases:
        '''

        queue = deque([(0,0,0)])
        ROWS = len(grid)
        COLS = len(grid[0])
        distance = [[float('inf') for _ in range(COLS)] for _ in range(ROWS)]

        dirs = [
            (0,1),
            (0,-1),
            (1,0),
            (-1,0)
        ]

        distance[0][0] = 0

        while queue:
            dist, cur_r, cur_c = queue.popleft()

            if dist > distance[cur_r][cur_c]:
                continue

            for idx, (dr,dc) in enumerate(dirs, start=1):
                nr = cur_r + dr
                nc = cur_c + dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                    continue

                cost = 0 if idx == grid[cur_r][cur_c] else 1
                new_dist = cost + dist
                if new_dist < distance[nr][nc]:
                    distance[nr][nc] = new_dist
                
                    if new_dist == dist:
                        queue.appendleft((new_dist,nr,nc))
                    else:
                        queue.append((new_dist,nr,nc))

        return distance[ROWS-1][COLS-1]

            
            

