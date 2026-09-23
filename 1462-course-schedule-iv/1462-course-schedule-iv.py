class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: list[list[int]], queries: list[list[int]]) -> list[bool]:
        
        dist = [[False]*numCourses for _ in range(numCourses)]

        for i in range(numCourses):
            dist[i][i] = True
        
        for u,v in prerequisites:
            dist[u][v] = True

        for k in range(numCourses):
            for i in range(numCourses):
                if not dist[i][k]:
                    continue
                for j in range(numCourses):
                    dist[i][j] = dist[i][j] or (dist[i][k] and dist[k][j])

        ans = []
        for u,v in queries:
            ans.append(dist[u][v])
        
        return ans