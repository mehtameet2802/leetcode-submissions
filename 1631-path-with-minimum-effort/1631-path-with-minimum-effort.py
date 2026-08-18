class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS = len(heights)
        COLS = len(heights[0])
        dirs = [[0,1],[1,0],[-1,0],[0,-1]]
        min_heap = []
        effort = [[float('inf')]*COLS for _ in range(ROWS)]

        effort[0][0] = 0

        heapq.heappush(min_heap,(0,0,0))

        while min_heap:
            e,r,c = heapq.heappop(min_heap)

            if r == ROWS-1 and c==COLS-1:
                return e

            for dr,dc in dirs:
                nr = r + dr
                nc = c + dc

                if nr<0 or nc<0 or nr>=ROWS or nc>=COLS:
                    continue
                
                w = abs(heights[r][c] - heights[nr][nc])
                ne = max(e,w)

                if effort[nr][nc] > ne:
                    effort[nr][nc] = ne
                    heapq.heappush(min_heap,(ne,nr,nc))

                
        return effort[ROWS-1][COLS-1]