class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        INF = float('inf')
        n = numCourses

        dist = [[INF]*n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u,v in prerequisites:
            dist[u][v] = min(dist[u][v],1)

        
        for k in range(n):
            for i in range(n):
                for j in range(n):

                    if dist[i][k] == INF or dist[k][j]==INF:
                        continue
                    
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )
        
        ans = []
        for a,b in queries:
            if dist[a][b] == INF:
                ans.append(False)
            else:
                ans.append(True)

        return ans