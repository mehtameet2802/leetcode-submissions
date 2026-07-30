from collections import defaultdict,deque

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = defaultdict(list)

        for ele,w in zip(equations,values):
            u, v = ele[0], ele[1]
            graph[u].append((v,w))
            graph[v].append((u,1/w))


        def helper(s,e):
            queue = deque([])
            queue.append((s,1))
            visited = set()
            
            while queue:
                
                ele = queue.popleft()
                visited.add(ele[0])
                
                for nei, nei_w in graph[ele[0]]:
                    
                    if nei in visited:
                        continue

                    n_w = ele[1]*nei_w

                    if nei == e:
                        return n_w
                    
                    queue.append((nei,n_w))
            
            return -1
        ans = []
        for s,e in queries:
            if s not in graph or e not in graph:
                ans.append(float(-1))
            elif s == e:
                ans.append(float(1))
            else:
                ans.append(helper(s,e))

        return ans