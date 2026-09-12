class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        Required output:
        What represents a node? - a point represnets a node
        What represents an edge? - a path from one point to other is edge 
        How is an edge cost calculated? - its the manhattan distance
        What properties must the final connections satisfy? - overall cost of creating all the connetions must be least
        Would a cycle ever improve the answer? - no
        Brute-force approach: fo each node calculate the minimum distance to all the other nodes and take the edeg for a node not reach yet and has the minimum distance 
        Pattern prediction: MST, Prims
        State/data structures required:
        Decision rule:
        Invariant:
        Expected TC and SC:
        '''

        '''
        will create an undirected graph
        have a set visited
        take the first node and push in min heap
        while min_heap
        get the first node if not in visisted, iterate all its nei and add the manhattan dist of reaching all nei in min_heap
        do this until all the nodes reached and add the cost to get the final ans

        while writing code realized we did not have edges, we have points,
        so first we take point 0, calculate dist from point 0 to all the other points and push in min_heap
        while min_heap, I get the point with min dist and if not visited calculate the dist from that point to all the remaining points and push in min_heap
        when getting points from min_heap add the dist to ans
        '''

        
        visited = set()
        min_heap = []
        heapq.heappush(min_heap,(0,points[0][0],points[0][1]))
        
        points_set = set()

        for x,y in points:
            points_set.add((x,y))

        ans = 0

        while min_heap:
            d, x, y = heapq.heappop(min_heap)

            if (x,y) in visited:
                continue

            ans += d
            
            visited.add((x,y))
            points_set.remove((x,y))

            for nx, ny in points_set:
                if (nx,ny) in visited:
                    continue
                dist = abs(nx-x) + abs(ny-y)
                heapq.heappush(min_heap, (dist,nx,ny))
        
        return ans





