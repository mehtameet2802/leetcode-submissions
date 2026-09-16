class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        '''
        dist[i][j] represents: - dist from node i to j
        Initial diagonal values: - 0
        Initial edge values: - float(inf)
        Intermediate-node invariant:
        Update formula: - if from i to k and k to j sum is less than dist from i to j
        Tie-breaking rule:
        Expected TC: O(V^3)
        Expected SC: O(V+E)
        '''
        ROWS = n
        dist = [[float('inf') for i in range(n)] for j in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u,v,w in edges:
            dist[u][v] = w
            dist[v][u] = w

        for k in range(n):
            for i in range(n):
                for j in range(n):
                    if dist[i][k]==float('inf') or dist[k][j]==float('inf'):
                        continue
                    
                    dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])


        min_cnt = n
        ans = -1

        for i in range(n):
            cur_cnt = 0 

            for j in range(n):
                if j!=i and dist[i][j] <= distanceThreshold:
                    cur_cnt += 1
            
            if cur_cnt <= min_cnt:
                min_cnt = cur_cnt
                ans = i

        return ans


