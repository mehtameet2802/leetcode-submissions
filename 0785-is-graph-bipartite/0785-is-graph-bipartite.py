class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        What does each node’s state represent?
        When is a neighboring node valid?
        What exact condition proves failure?
        When should state be assigned?
        How will disconnected components be handled?
        Invariant:
        Complexity:
        '''
        n = len(graph)
        color = [-1]*n

        for node in range(n):
            if color[node] != -1:
                continue
            
            color[node] = 0
            queue = deque([node])

            while queue:
                cur_node = queue.popleft()

                for nei in graph[cur_node]:
                    if color[nei] == color[cur_node]:
                        return False
                    
                    if color[nei] != -1:
                        continue
                    
                    color[nei] = 1 - color[cur_node]
                    queue.append(nei)
        
        return True

