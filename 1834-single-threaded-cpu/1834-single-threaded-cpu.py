class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        min_heap = []
        
        # Store original index
        tasks = [
            (start, duration, idx)
            for idx, (start, duration) in enumerate(tasks)
        ]
        tasks.sort(key = lambda x: x[0])

        n = len(tasks)
        time = 0
        i = 0
        ans = []

        while i < n or min_heap:
            if not min_heap:
                time = max(time, tasks[i][0])
            
            while i < n and tasks[i][0] <= time:
                heapq.heappush(min_heap, (tasks[i][1], tasks[i][2]))
                i += 1

            time_taken, idx = heapq.heappop(min_heap)
            time += time_taken
            ans.append(idx)

        return ans