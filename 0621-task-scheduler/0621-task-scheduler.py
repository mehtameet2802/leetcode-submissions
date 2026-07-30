import heapq
from collections import deque, Counter

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        t_map = Counter(tasks)

        max_heap = []

        for t,c in t_map.items():
            heapq.heappush(max_heap,-c)
        
        queue = deque([])

        time = 0
        while max_heap or queue:

            time+=1

            if max_heap:
                c = heapq.heappop(max_heap)
                c+=1

                if c!=0:
                    queue.append((c,time+n))
            
            if queue and queue[0][1] == time:
                ele = queue.popleft()
                heapq.heappush(max_heap,ele[0])
        
        return time


