class Solution:
    def countPaths(self, n: int, roads: list[list[int]]) -> int:

        graph = defaultdict(list)

        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        time = [float('inf')]*n
        cnt = [0]*n

        time[0] = 0
        cnt[0] = 1
        min_heap = []
        heapq.heappush(min_heap,(0,0))

        while min_heap:
            cur_time, node = heapq.heappop(min_heap)

            if cur_time > time[node]:
                continue
            
            for nei,w in graph[node]:
                new_time = cur_time + w

                if new_time < time[nei]:
                    cnt[nei] = cnt[node]
                    time[nei] = new_time
                    heapq.heappush(min_heap,(new_time, nei))
                elif new_time == time[nei]:
                    cnt[nei] += cnt[node]
        
        return cnt[n-1] % (pow(10,9)+7)
        



