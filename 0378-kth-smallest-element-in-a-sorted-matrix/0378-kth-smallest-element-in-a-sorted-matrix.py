class Solution:
    def kthSmallest(self, matrix: list[list[int]], k: int) -> int:
        r = len(matrix)

        min_heap = []

        for i in range(r):
            heapq.heappush(min_heap,(matrix[i][0],i,0))
        
        cnt = 0

        while cnt < k-1:
            ele, row_idx, ele_idx = heapq.heappop(min_heap)

            if ele_idx+1 < len(matrix[0]):
                heapq.heappush(min_heap, (matrix[row_idx][ele_idx+1], row_idx, ele_idx+1))
            
            cnt += 1
            
        return min_heap[0][0]