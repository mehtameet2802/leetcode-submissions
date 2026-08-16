class Solution:
    def numSquares(self, n: int) -> int:
        # target = n
        # ans = n

        # def helper(i, cur, cnt):
        #     nonlocal ans

        #     if i*i > n:
        #         return

        #     if cur > n:
        #         return
            
        #     if cur == n:
        #         ans = min(ans,cnt)
        #         return
            
        #     helper(i+1, cur, cnt)
        #     helper(i, cur + i**2, cnt+1)
        
        # helper(1, 0, 0)
        # return ans

        # dp = {}

        # def helper(i, cur):

        #     if (i,cur) in dp:
        #         return dp[(i,cur)]

        #     if i*i > n:
        #         return float('inf')

        #     if cur > n:
        #         return float('inf')
            
        #     if cur == n:
        #         return 0
            
        #     a1 = helper(i+1, cur)
        #     a2 = helper(i, cur + i**2) + 1

        #     ans = min(a1,a2)
        #     dp[(i,cur)] = ans
        #     return ans

        
        # return helper(1, 0)


        dp = {}

        def helper(rem):

            if rem == 0:
                return 0

            if rem in dp:
                return dp[rem]
            
            ans = float('inf')

            for i in range(1, int(rem ** 0.5)+1):
                ans = min(
                    ans,
                    1 + helper(rem - i*i)
                )
            
            dp[rem] = ans
            return ans

        return helper(n)

        