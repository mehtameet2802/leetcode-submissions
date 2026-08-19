class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        total = 0
        n = len(points)
        visited = [False]*n
        min_heap = []
        heapq.heappush(min_heap,(0,0))
        count = 0

        while count < n:
            cost, i = heapq.heappop(min_heap)

            if visited[i]:
                continue
            
            visited[i] = True
            total += cost
            count += 1

            x1, y1 = points[i]

            for j in range(n):

                if visited[j]:
                    continue

                x2, y2 = points[j]

                d = abs(x1-x2) + abs(y1-y2)

                heapq.heappush(min_heap,(d,j))

        
        return total