class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n==1:
            return [0]

        indegree = [0]*n
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

            indegree[u] += 1
            indegree[v] += 1
        
        queue = deque([])

        remaining = n

        for i,degree in enumerate(indegree):
            if degree == 1:
                queue.append(i)

        remaining = n
        while remaining > 2:
            length = len(queue)
            remaining -= length

            for _ in range(length):

                leaf = queue.popleft()

                for nei in graph[leaf]:
                    indegree[nei] -=1 

                    if indegree[nei] == 1:
                        queue.append(nei)
        
        return list(queue)


