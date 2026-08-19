class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        
#         cost = [float('inf')]*n

#         graph = defaultdict(list)
#         for u,v,w in flights:
#             graph[u].append((v,w))

#         queue = deque([])
#         queue.append((src,0))

#         cost = [[float('inf')]*(k+2) for _ in range(n)]
#         cost[src][0] = 0

#         while queue:
#             src, depth = queue.popleft()

#             if depth == k+1:
#                 continue

#             for nei, weight in graph[src]:
#                 if cost[src][depth] + weight > cost[nei][depth + 1]:
#                     continue
                
#                 cost[nei][depth+1] = cost[src][depth] + weight
#                 queue.append((nei,depth+1))
        
#         return min(cost[dst]) if min(cost[dst]) != float('inf') else -1

        cost = [float('inf')]*n
        cost[src] = 0

        for _ in range(k+1):

            new_cost = cost[:]

            for u,v,w in flights:
                if cost[u] == float('inf'):
                    continue

                if cost[u] + w > new_cost[v]:
                    continue

                new_cost[v] = cost[u]+w 
            
            cost = new_cost
        
        return -1 if cost[dst] == float('inf') else cost[dst]
        

