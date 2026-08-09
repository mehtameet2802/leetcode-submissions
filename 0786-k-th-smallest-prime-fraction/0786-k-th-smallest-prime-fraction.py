class Solution:
    def kthSmallestPrimeFraction(self, arr: List[int], k: int) -> List[int]:

        '''
        Pattern:
        - K-Way Merge
        - Min Heap
        - Each denominator creates a sorted stream

        TC - O(n log n + k log n)
        SC - O(n)
        '''

        min_heap = []
        n = len(arr)

        for j in range(1,n):
            heapq.heappush(
                min_heap,
                (arr[0]/arr[j],0,j)
            )
        
        while k>1:
            val, idx, j = heapq.heappop(min_heap)

            if idx+1 < j:
                heapq.heappush(
                    min_heap,
                    (arr[idx+1]/arr[j], idx+1, j)
                )

            k -= 1
        
        ele = heapq.heappop(min_heap)
        return [arr[ele[1]],arr[ele[2]]]