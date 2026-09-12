class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        Required output:
        Graph direction: directed
        Meaning of an edge: time to reach the other node
        Are all edge costs equal? - no
        What does the state for each node represent? 
        What makes a candidate state better?
        When can a node’s result be considered final?
        Data structure needed:
        InvariantInvariant invariant:
        Danger update rule:
        DangerExpected return value:
        ExpectedExpected complexity3?
        ExpectedExpected complexity:
        ``Expected complexity:
        Expected complexity:
        '''

        dist = [float('inf')]*(n+1)

        graph = defaultdict(list)

        for u,v,w in times:
            graph[u].append((v,w))

        min_heap = []
        heapq.heappush(min_heap, (0,k))
        dist[k] = 0

        while min_heap:
            cur_dist, node = heapq.heappop(min_heap)

            for nei, weight in graph[node]:

                nei_dist = cur_dist + weight

                if nei_dist < dist[nei]:
                    dist[nei] = nei_dist
                    heapq.heappush(min_heap, (nei_dist, nei))

        ans = -float('inf')
        for node in range(1,n+1):
            if dist[node] == float('inf'):
                return -1
            ans = max(ans,dist[node])

        return ans 