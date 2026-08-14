class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:

        graph = defaultdict(list)

        for u,v in edges:
            graph[u].append(v)
            graph[v].append(u)

        n = len(graph)
        
        for node, edges in graph.items():
            if len(edges) == n - 1:
                return node
        
        return -1