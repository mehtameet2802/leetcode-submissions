class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        color = [-1]*n
        

        for i in range(n):
            queue = deque()

            if color[i] != -1:
                continue
            
            color[i] = 0
            queue.append(i)

            while queue:
                node = queue.popleft()

                for nei in graph[node]:
                    if color[nei] == color[node]:
                        return False
                    
                    if color[nei] != -1:
                        continue
                    
                    color[nei] = 1-color[node]
                    queue.append(nei)
            
        return True
