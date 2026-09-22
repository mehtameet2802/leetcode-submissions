class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        indegree = [0] * numCourses

        for v,u in prerequisites:
            graph[u].append(v)
            indegree[v] += 1

        queue = deque()
        
        for i, val in enumerate(indegree):
            if val == 0:
                queue.append(i)

        nodes_cnt = len(queue)
        while queue:
            node = queue.popleft()

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    nodes_cnt += 1
                    queue.append(nei)
        
        return nodes_cnt == numCourses
