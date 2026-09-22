class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])

        min_heap = []

        for i in range(ROWS):
            heapq.heappush(min_heap,(matrix[i][0],i,0))
        
        cnt = 0

        while cnt < k-1:
            ele, row_idx, col_idx = heapq.heappop(min_heap)
            
            new_col_idx = col_idx + 1
            if new_col_idx < COLS:
                heapq.heappush(min_heap, (matrix[row_idx][col_idx+1], row_idx, new_col_idx))
            
            cnt += 1
            
        return min_heap[0][0]