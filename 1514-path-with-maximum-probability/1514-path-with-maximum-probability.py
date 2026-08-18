class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        max_heap = []

        graph = defaultdict(list)

        for node, prob in zip(edges,succProb):
            a,b = node
            graph[a].append((b,prob))
            graph[b].append((a,prob))
        
        heapq.heappush(max_heap,(-1.0,start_node))

        ans = [0]*n
        ans[start_node] = 1

        while max_heap:
            prob, node = heapq.heappop(max_heap)
            prob = -prob

            for v, p in graph[node]:
                np = prob * p

                if ans[v] < np:
                    ans[v] = np
                    heapq.heappush(max_heap,(-np,v))
        
        return ans[end_node]
