class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        color = [-1]*(n+1)

        graph = defaultdict(list)
        
        for a,b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        for i in range(1,n+1):

            if color[i] != -1:
                continue
            
            color[i] = 0
            q = deque([i])

            while q:
                u = q.popleft()

                for v in graph[u]:
                    if color[v] == color[u]:
                        return False
                    elif color[v] == -1:
                        color[v] = 1-color[u]
                        q.append(v)
        
        return True

            
        
