class Solution:
    def fillCups(self, amount: List[int]) -> int:
        '''
        Pattern:
        - Greedy + Max Heap

        N= 3, so we can constant

        TC - O(N log N)
        SC - O(N)

        N = len(amount)
        '''

        max_heap = [-num for num in amount if num > 0]
        heapq.heapify(max_heap)

        ans = 0

        while max_heap:
            ele1 = heapq.heappop(max_heap)
            
            if max_heap:
                ans += 1
                ele2 = heapq.heappop(max_heap)
                
                if ele1 + 1 < 0:
                    heapq.heappush(max_heap, ele1 + 1)
                
                if ele2 + 1 < 0:
                    heapq.heappush(max_heap, ele2 + 1)
            else:
                ans -= ele1
    
        
        return ans
