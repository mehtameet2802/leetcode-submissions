class Solution:
    def minGroups(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        
        min_heap = []
        
        ans = 0

        for i in range(len(intervals)):
            if not min_heap:
                heapq.heappush(min_heap, intervals[i][1])
            else:
                if min_heap[0] < intervals[i][0]:
                    heapq.heappop(min_heap)
                    heapq.heappush(min_heap, intervals[i][1])
                else:
                    heapq.heappush(min_heap, intervals[i][1])
            
            ans = max(ans, len(min_heap))

        return ans
