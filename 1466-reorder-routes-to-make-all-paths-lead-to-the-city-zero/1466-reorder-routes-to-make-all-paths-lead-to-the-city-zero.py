class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        # visited = set()
        # graph = defaultdict(list)
        
        # for u,v in connections:
        #     graph[u].append((v,1))
        #     graph[v].append((u,0))


        # def helper(node):
        #     visited.add(node)

        #     count = 0
        #     for nei, cost in graph[node]:
        #         if nei in visited:
        #             continue
                
        #         count += cost
        #         count += helper(nei)
            
        #     return count
        
        # return helper(0)


        stack = [0]
        visited = {0}
        cnt = 0
        graph = defaultdict(list)
        
        for u,v in connections:
            graph[u].append((v,1))
            graph[v].append((u,0))

        while stack:
            node = stack.pop()
            visited.add(node)
            count = 0
            for nei, cost in graph[node]:
                if nei in visited:
                    continue
                
                cnt += cost
                stack.append(nei)

        return cnt