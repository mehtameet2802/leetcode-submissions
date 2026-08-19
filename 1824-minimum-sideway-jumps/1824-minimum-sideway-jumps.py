class Solution:
    def minSideJumps(self, obstacles: List[int]) -> int:
        dp = [1,0,1]

        for i in range(len(obstacles)):

            blocked = obstacles[i]

            if blocked != 0:
                dp[blocked-1] = float('inf')

            for j in range(3):
                if j == blocked - 1:
                    continue

                dp[j] = min(
                    dp[j],
                    min(dp)+1
                ) 
        
        return min(dp)