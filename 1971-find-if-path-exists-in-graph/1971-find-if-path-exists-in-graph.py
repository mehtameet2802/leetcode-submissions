class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)
        
        visited = set()

        def find_dest(node, target):
            if node == target:
                return True
            
            visited.add(node)

            for v in graph[node]:
                if v not in visited:
                    if find_dest(v, target):
                        return True
            
            return False
        
        return find_dest(source, destination)
            