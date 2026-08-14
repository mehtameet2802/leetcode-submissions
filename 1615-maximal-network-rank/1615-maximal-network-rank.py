class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        in_degree = [0]*n
        connected = set()

        for u, v in roads:
            in_degree[u] += 1
            in_degree[v] += 1
            connected.add((u,v))
            connected.add((v,u))

        ans = 0
        for i in range(n):
            for j in range(i+1, n):
                rank = in_degree[i] + in_degree[j]

                if (i,j) in connected:
                    rank -= 1
                
                ans = max(ans, rank)
        
        return ans