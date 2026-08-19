class Solution:
    def minimumCost(self, source: str, target: str, original: List[str], changed: List[str], cost: List[int]) -> int:
        
        INF = float('inf')
        n = 26

        dist = [[INF]*n for _ in range(n)]

        for i in range(n):
            dist[i][i] = 0

        for u,v,c in zip(original,changed,cost):
            dist[ord(u)-ord('a')][ord(v)-ord('a')] = min(dist[ord(u)-ord('a')][ord(v)-ord('a')],c)

        
        for k in range(n):
            for i in range(n):
                for j in range(n):

                    if dist[i][k] == INF or dist[k][j]==INF:
                        continue
                    
                    dist[i][j] = min(
                        dist[i][j],
                        dist[i][k] + dist[k][j]
                    )

        cost = 0
        for i in range(len(source)):
            if dist[ord(source[i])-ord('a')][ord(target[i])-ord('a')] == INF:
                return -1
            
            cost += dist[ord(source[i])-ord('a')][ord(target[i])-ord('a')]
        
        return cost
        