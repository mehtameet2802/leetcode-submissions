class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        indegree = [0] * numCourses
        graph = defaultdict(list)

        for u,v in prerequisites:
            indegree[u] += 1
            graph[v].append(u)
        
        queue = deque([])
        visited = []

        for i, degree in enumerate(indegree):
            if degree == 0:
                queue.append(i)
                visited.append(i)

        
        while queue:

            length = len(queue)

            for _ in range(length):
                course = queue.popleft()

                for nei in graph[course]:
                    indegree[nei] -= 1

                    if indegree[nei] == 0:
                        queue.append(nei)
                        visited.append(nei)
        
        if len(visited) != numCourses:
            return []

        return visited
        
