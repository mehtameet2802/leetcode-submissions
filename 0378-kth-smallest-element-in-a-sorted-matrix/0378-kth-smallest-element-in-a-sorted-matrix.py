class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:

        '''
        Pattern:
        - K-Way Merge
        - Min Heap
        - Treat each row as a sorted list
        - Keep one candidate from each row

        TC:
        O(k log n)

        There are n rows, so the heap has at most n elements.
        Each pop/push costs O(log n).
        We perform k pops.

        SC:
        O(n)

        The heap contains at most one element from
        each of the n rows.
        '''
        min_heap = []

        for i in range(len(matrix)):
            heapq.heappush(min_heap, (matrix[i][0], i, 0))
        
        while k>1:
            val, row, ele = heapq.heappop(min_heap)

            if ele + 1 < len(matrix[row]):
                heapq.heappush(min_heap, (matrix[row][ele+1],row,ele+1))
            
            k -= 1
        
        return heapq.heappop(min_heap)[0]