class Solution:
    def gardenNoAdj(self, n: int, paths: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for a,b in paths:
            graph[a].append(b)
            graph[b].append(a)
        
        color = [-1]*n

        for i in range(1,n+1):

            if color[i-1] != -1:
                continue
            
            seen = set()
            for v in graph[i]:
                seen.add(color[v-1])
            
            for j in range(1,5):
                if j not in seen:
                    color[i-1] = j
                    break
        
        return color
