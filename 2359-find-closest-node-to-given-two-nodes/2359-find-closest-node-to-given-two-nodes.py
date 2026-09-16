class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        
        # distance = [[float('inf') for _ in range(len(edges))] for _ in range(2)]
        # graph = defaultdict(list)

        # for u,v in enumerate(edges):
        #     if v == -1:
        #         continue
        #     graph[u].append(v)
        
        # def djikstar(node_idx, node):
        #     distance[node_idx][node] = 0

        #     min_heap = []
        #     heapq.heappush(min_heap, (0,node))

        #     while min_heap:
        #         dist, cur_node = heapq.heappop(min_heap)

        #         if distance[node_idx][cur_node] < dist:
        #             continue
                
        #         for nei in graph[cur_node]:
        #             new_dist = dist + 1

        #             if new_dist < distance[node_idx][nei]:
        #                 distance[node_idx][nei] = new_dist
        #                 heapq.heappush(min_heap, (new_dist,nei))
            
        
        # djikstar(0, node1)
        # djikstar(1, node2)
        # ans = float('inf')
        # min_idx = 0

        # for i in range(len(edges)):
        #     if distance[0][i] == float('inf') or distance[1][i] == float('inf'):
        #         continue

        #     cur_max_dist = max(distance[0][i], distance[1][i])
        #     if ans > cur_max_dist:
        #         ans = cur_max_dist
        #         min_idx = i

        # return -1 if ans == float('inf') else min_idx


        distance = [[float('inf') for _ in range(len(edges))] for _ in range(2)]
        
        def get_dist(node_idx, node):
            cur_node = node
            dist = 0

            while cur_node != -1 and distance[node_idx][cur_node] == float('inf'):
                distance[node_idx][cur_node] = dist
                cur_node = edges[cur_node]
                dist += 1
            
        
        get_dist(0, node1)
        get_dist(1, node2)
        ans = float('inf')
        min_idx = 0

        for i in range(len(edges)):
            if distance[0][i] == float('inf') or distance[1][i] == float('inf'):
                continue

            cur_max_dist = max(distance[0][i], distance[1][i])
            if ans > cur_max_dist:
                ans = cur_max_dist
                min_idx = i

        return -1 if ans == float('inf') else min_idx



