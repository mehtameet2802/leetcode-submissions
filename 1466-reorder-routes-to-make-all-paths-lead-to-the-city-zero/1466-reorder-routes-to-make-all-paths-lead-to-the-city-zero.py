class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        visited = set()
        graph = defaultdict(list)
        
        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))


        def helper(node):
            visited.add(node)

            count = 0
            for nei, cost in graph[node]:
                if nei in visited:
                    continue
                
                count += cost
                count += helper(nei)
            
            return count
        
        return helper(0)
        
