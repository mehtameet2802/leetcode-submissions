class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        '''
        Pattern:
        - Heap Scheduling
        - Greedy
        - Sort by start day
        - Min Heap stores end days
        - Each day attend the event
          with the earliest end day

        TC - O(N log N)
        SC - O(N)
        '''
        events.sort(key = lambda x:x[0])
        
        n = len(events)
        day = 0
        i = 0
        ans = 0
        min_heap = []

        while i<n or min_heap:

            if not min_heap:
                day = events[i][0]
            
            while i < n and events[i][0] <= day:
                heapq.heappush(min_heap, events[i][1])
                i += 1
            
            while min_heap and min_heap[0] < day:
                heapq.heappop(min_heap)

            if min_heap:
                heapq.heappop(min_heap)
                ans += 1
                day += 1
            
        return ans

