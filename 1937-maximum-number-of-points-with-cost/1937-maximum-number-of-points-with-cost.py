class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        # ROWS = len(points)
        # COLS = len(points[0])

        # dp = {}

        # def helper(r,c):
            
        #     if (r,c) in dp:
        #         return dp[(r,c)]

        #     if c<0 or r>=ROWS or c>=COLS:
        #         return -float('inf')
            
        #     if r == ROWS-1:
        #         return points[r][c]
            
        #     ans = -float('inf')
        #     for i in range(COLS):
        #         ans = max(ans, helper(r+1,i) - abs(c-i))
            
        #     dp[(r,c)] = ans + points[r][c]
        #     return dp[(r,c)]
        
        # result = -float('inf')
        # for i in range(COLS):
        #     result = max(result,helper(0,i))
        
        # return result


        ROWS = len(points)
        COLS = len(points[0])

        dp = points[0][:]

        for r in range(1,ROWS):
            left = [0]*COLS
            right = [0]*COLS

            left[0] = dp[0]

            for c in range(1,COLS):
                left[c] = max(
                    dp[c],
                    left[c-1]-1
                )
            
            right[COLS-1] = dp[COLS-1]

            for c in range(COLS-2,-1,-1):
                right[c] = max(
                    dp[c],
                    right[c+1]-1
                )
            
            for c in range(COLS):
                dp[c] = max(right[c],left[c])+points[r][c]

        return max(dp)

