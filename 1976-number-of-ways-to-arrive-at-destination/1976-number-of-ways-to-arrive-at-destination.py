class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u,v,w in roads:
            graph[u].append((v,w))
            graph[v].append((u,w))
        
        ans = [(float('inf'),0)] * n
        ans[0] = (0,1)
        min_heap = []

        heapq.heappush(min_heap, (0,0))

        while min_heap:
            t, node = heapq.heappop(min_heap)

            if t > ans[node][0]:
                continue

            for nei, time in graph[node]:
                new_time = time + t

                if new_time == ans[nei][0]:
                    ans[nei] = (ans[nei][0], (ans[node][1]+ans[nei][1])%(pow(10,9)+7))
                    continue
                
                elif new_time < ans[nei][0]:
                    ans[nei] = (new_time,ans[node][1])
                    heapq.heappush(min_heap, (new_time, nei))

        return ans[n-1][1]
