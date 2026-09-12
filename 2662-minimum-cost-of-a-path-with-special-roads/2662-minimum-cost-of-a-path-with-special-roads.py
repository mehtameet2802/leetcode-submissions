class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        '''
        Required output: MIn cost of going from start to target using special roads
        Brute-force approach: 
        Pattern prediction: Djikstar
        What does one state represent?
        Which coordinates could matter to the optimal path? start, target and the coordinates that can be achieved in min cost in between start and target and can help reach the target from start
        What movement options exist from a state? from 1 state go to all the other states wherever the special roads take you
        Are all costs equal? No
        What data structure should manage candidate states? - min_heap, graph, later recollected and identified a distance dict will be required
        Decision rule:
        Invariant:
        Termination condition: reached target, or no road forward
        Expected TC and SC:

        previouslt
        though FLoyd Warsahll as through needed to get dist from each node to every other node and the use intermediate state
        Which coordinates could matter to the optimal path? start target and mostly intermidiate
        '''

        # graph = defaultdict(set)
        # dist = {}
        # min_heap = []
        # start_x, start_y = start[0], start[1]
        # target_x, target_y = target[0], target[1]

        # for x1,y1,x2,y2,w in specialRoads:
        #     graph[(x1,y1)].add((x2,y2,w))
            
        #     start_to_road = abs(start_x-x1) + abs(start_y-y1)
        #     graph[(start_x,start_y)].add((x1,y1,start_to_road))

        #     road_to_target = abs(target_x-x2) + abs(target_y-y2)
        #     graph[(x2,y2)].add((target_x,target_y,road_to_target))

        #     dist[(x1,y1)] = float('inf')
        #     dist[(x2,y2)] = float('inf')

        # start_to_target = abs(target_x-start_x) + abs(target_y-start_y)
        # graph[(start_x,start_y)].add((target_x,target_y,start_to_target))
        
        # dist[target[0],target[1]] = float('inf')
        # dist[start[0],start[1]] = 0
        # heapq.heappush(min_heap,(0,start[0],start[1]))

        # print(dist)
        # print(graph)

        # while min_heap:
        #     d,x,y = heapq.heappop(min_heap)

        #     for nei_x, nei_y, nei_w in graph[(x,y)]:
        #         nei_d = d + nei_w

        #         if nei_d < dist[(nei_x, nei_y)]:
        #             dist[(nei_x, nei_y)] = nei_d
        #             heapq.heappush(min_heap, (nei_d,nei_x,nei_y))
                
        #         print(dist)
        
        # return dist[target[0],target[1]]

        def manhattan_dist(x1,y1,x2,y2):
            return abs(x1-x2) + abs(y1-y2)

        dist = {}
        min_heap = []        
        dist[start[0],start[1]] = 0
        target_x, target_y = target[0], target[1]
        heapq.heappush(min_heap,(0,start[0],start[1]))
        ans = float('inf')

        while min_heap:
            pos_cost,pos_x,pos_y = heapq.heappop(min_heap)

            if pos_cost > dist[(pos_x,pos_y)]:
                continue

            ans = min(ans, pos_cost + manhattan_dist(pos_x,pos_y,target_x,target_y))

            for path_x1,path_y1,path_x2,path_y2,path_cost in specialRoads:

                road_cost = min(path_cost, manhattan_dist(path_x1,path_y1,path_x2,path_y2))

                new_pos_cost = road_cost + manhattan_dist(pos_x,pos_y,path_x1,path_y1) + pos_cost

                if new_pos_cost < dist.get((path_x2,path_y2),float('inf')):
                    dist[(path_x2, path_y2)] = new_pos_cost
                    heapq.heappush(min_heap, (new_pos_cost, path_x2, path_y2))
        
        return ans
