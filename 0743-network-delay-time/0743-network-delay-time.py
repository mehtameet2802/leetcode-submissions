class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        ans = [float('inf')] *n
        ans[k-1] = 0

        graph = defaultdict(list)

        for a,b,w in times:
            graph[a].append((b,w))

        min_heap = []
        heapq.heappush(min_heap,(0,k))

        while min_heap:
            dist, node = heapq.heappop(min_heap)

            for nei, d in graph[node]:
                if ans[nei-1] < dist:
                    continue
                
                new_dist = d + dist

                if ans[nei-1] > new_dist:
                    ans[nei-1] = new_dist
                    heapq.heappush(min_heap,(new_dist, nei))
        
        if float('inf') in ans:
            return -1
        
        return max(ans)
