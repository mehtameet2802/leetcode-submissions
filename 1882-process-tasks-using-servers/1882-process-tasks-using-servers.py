class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        available = [(server, idx) for idx,server in enumerate(servers)]
        heapq.heapify(available)

        min_heap = []

        ans = [-1]*len(tasks)
        current_time = 0

        for i, task in enumerate(tasks):

            current_time = max(current_time,i)
            
            while min_heap and min_heap[0][0] <= i:
                end, server_idx = heapq.heappop(min_heap)
                heapq.heappush(available,(servers[server_idx],server_idx))
            
            if not available:
                current_time = min_heap[0][0]

                while min_heap and min_heap[0][0] <= current_time:
                    end, server_idx = heapq.heappop(min_heap)
                    heapq.heappush(available,(servers[server_idx],server_idx))
            
            server, server_idx = heapq.heappop(available)
            ans[i] = server_idx

            finish_time = current_time + task

            heapq.heappush(min_heap, (finish_time,server_idx))
        

        return ans
        

