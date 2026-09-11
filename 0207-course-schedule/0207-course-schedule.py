class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0]*numCourses
        visitedNodes = 0

        for u,v in prerequisites:
            graph[v].append(u)
            indegree[u] += 1
        
        queue = deque()

        for idx, degree in enumerate(indegree):
            if degree == 0:
                queue.append(idx)
        
        while queue:
            node = queue.popleft()
            visitedNodes += 1

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    queue.append(nei)
        
        if visitedNodes == numCourses:
            return True
        
        return False
        
