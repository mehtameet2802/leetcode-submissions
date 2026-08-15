class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        outdegree = [0]*len(graph)
        reverse = defaultdict(list)
        
        for i, node in enumerate(graph):
            outdegree[i] = len(node)

            for nei in graph[i]:
                reverse[nei].append(i)
        
        queue = deque([])

        for node, degree in enumerate(outdegree):
            if degree == 0:
                queue.append(node)

        safe = []

        while queue:
            length = len(queue)

            for _ in range(length):
                node = queue.popleft()
                safe.append(node)

                for nei in reverse[node]:
                    outdegree[nei] -= 1

                    if outdegree[nei] == 0:
                        queue.append(nei)
        
        return sorted(safe)