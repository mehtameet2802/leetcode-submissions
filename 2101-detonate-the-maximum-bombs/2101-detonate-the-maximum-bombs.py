class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        
        n = len(bombs)
        reachable = [[False]*n for _ in range(n)]

        for i in range(n):
            reachable[i][i] = True

        for i in range(n):
            x1,y1,r1 = bombs[i]

            for j in range(n):
                if i == j:
                    continue

                x2,y2,r2 = bombs[j]

                dx = x1-x2
                dy = y1-y2

                if dx*dx + dy*dy <= r1*r1:
                    reachable[i][j] = True
        
        for k in range(n):
            for i in range(n):
                for j in range(n):
                    reachable[i][j] = reachable[i][j] or (reachable[i][k] and reachable[k][j])
        
        ans = 0

        for i in range(n):
            ans = max(ans, sum(reachable[i]))
        return ans

