class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        # seen = defaultdict(int)

        # dirs = [[0,1],[1,0]]

        # def helper(r,c):
        #     if (r,c) in seen:
        #         return seen[(r,c)]
            
        #     if r==m-1 and c==n-1:
        #         return 1

        #     paths = 0
        #     for dr,dc in dirs:
        #         nr = r + dr
        #         nc = c + dc

        #         if nr<0 or nc<0 or nr>=m or nc>=n:
        #             continue
                
        #         paths += helper(nr,nc)

        #     seen[(r,c)] = paths
            
        #     return paths
        
        # return helper(0,0)


        '''
        2D Dp
        '''
        # dp = [[0 for _ in range(n)] for _ in range(m)]

        # for j in range(n):
        #     dp[m-1][j] = 1
        
        # for i in range(m):
        #     dp[i][n-1] = 1

        # for i in range(m-2,-1,-1):
        #     for j in range(n-2,-1,-1):
        #         dp[i][j] = dp[i+1][j] + dp[i][j+1]
        
        # return dp[0][0]
        
        '''
        1D DP
        '''
        dp = [1]*n

        for i in range(m-1):
            for j in range(n-1,-1,-1):
                if j == n-1:
                    cur = dp[j]
                else:
                    cur = cur + dp[j]
                
                dp[j] = cur
        
        return dp[0]
            
