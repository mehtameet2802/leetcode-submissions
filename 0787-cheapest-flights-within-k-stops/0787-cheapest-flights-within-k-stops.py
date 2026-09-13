class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        Required output: min cost to reach dest from start given at max k stops

        What does k limit: stops or edges? k determines stops

        What must one state represent? - cur_node, cost, stops

        Why might distance[node] alone lose necessary information?

        Can ordinary BFS work? - No, as the prices are different

        Can ordinary node-only Dijkstra work safely? we midht need to store num of stops

        Pattern prediction:

        What information must be preserved between iterations?

        Invariant:

        Number of relaxation rounds:

        Expected TC and SC:

        Dangerous cases:
        - src == dst
        - direct flight
        - cheapest route uses too many stops
        - duplicate flights
        - unreachable destination
        '''

        # graph = defaultdict(list)
        # for u,v,w in flights:
        #     graph[u].append((v,w))

        # max_k = k+2
        # distance = [[float('inf'),max_k] for _ in range(n)]
        # min_heap = []
        # heapq.heappush(min_heap,(1,0,src))
        # distance[src] = [0,1]

        # while min_heap:
        #     cur_k, cur_dist, node = heapq.heappop(min_heap)

        #     if cur_k > max_k:
        #         continue

        #     if cur_dist > distance[node][0]:
        #         continue
            
        #     for nei, weight in graph[node]:
        #         new_dist = cur_dist + weight
        #         new_k = cur_k + 1

        #         if new_k > max_k:
        #             continue

        #         if new_dist > distance[nei][0]:
        #             continue

        #         distance[nei][0] = new_dist
        #         distance[nei][1] = cur_k + 1
        #         heapq.heappush(min_heap, (new_k, new_dist ,nei))
        
        # return -1 if distance[dst][0] == float('inf') else distance[dst][0]
        


        # graph = defaultdict(list)
        # for u,v,w in flights:
        #     graph[u].append((v,w))

        # max_k = k+2
        # distance = [[float('inf') for _ in range(max_k)]  for _ in range(n)]
        # min_heap = []
        # heapq.heappush(min_heap,(0,0,src))
        # distance[src][0] = 0

        # while min_heap:
        #     cur_dist, cur_k, node = heapq.heappop(min_heap)

        #     if cur_k >= max_k:
        #         continue

        #     if cur_dist > distance[node][cur_k]:
        #         continue
            
        #     for nei, weight in graph[node]:
        #         new_dist = cur_dist + weight
        #         new_k = cur_k + 1

        #         if new_k >= max_k:
        #             continue

        #         if new_dist < distance[nei][new_k]:
        #             distance[nei][new_k] = new_dist
        #             heapq.heappush(min_heap, (new_dist, new_k, nei))

        # min_dist = min(distance[dst])
        
        # return -1 if min_dist == float('inf') else min_dist

        costs = [float('inf') for _ in range(n)]
        costs[src] = 0

        for _ in range(k+1):
        
            new_costs = costs.copy()

            for start, dest, flight_cost in flights:
                if costs[start] == float('inf'):
                    continue

                new_cost = flight_cost + costs[start]

                if new_cost < new_costs[dest]:
                    new_costs[dest] = new_cost

            costs = new_costs

        if costs[dst] == float('inf'):
            return -1

        return costs[dst]           


