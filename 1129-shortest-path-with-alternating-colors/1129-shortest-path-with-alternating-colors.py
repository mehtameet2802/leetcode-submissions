class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)

        graph = [
            [[] for _ in range(n)],
            [[] for _ in range(n)] 
        ]

        for a,b in redEdges:
            graph[0][a].append(b)
        
        for a,b in blueEdges:
            graph[1][a].append(b)
        
        q = deque([(0,0,0),
            (0,0,1)
        ])

        ans = [-1] * n
        ans[0] = 0

        visited = set()

        while q:
            node, dist, color = q.popleft()

            new_color = 1-color

            for v in graph[new_color][node]:
                if (v,new_color) in visited:
                    continue

                if ans[v] == -1:
                    ans[v] = dist + 1
                visited.add((v,new_color))
                q.append((v,dist+1,new_color))
        

        return ans
        
        