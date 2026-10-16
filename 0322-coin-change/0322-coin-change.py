class Solution:
    # def coinChange(self, coins: list[int], amount: int) -> int:
        
    #     n = len(coins)
    #     def solve(i,cur):
    #         if cur == amount:
    #             return 0
            
    #         if cur > amount:
    #             return float('inf')
            
    #         if i>=n:
    #             return float('inf')
            
    #         skip = solve(i+1,cur)

    #         take = 1 + solve(i, cur+coins[i])

    #         return min(skip,take)
        
    #     ans = solve(0,0)

    #     return -1 if ans == float('inf') else ans

    # def coinChange(self, coins: list[int], amount: int) -> int:
        
    #     n = len(coins)
    #     dp = {}
    #     def solve(i,cur):
    #         if cur == amount:
    #             return 0
            
    #         if cur > amount:
    #             return float('inf')
            
    #         if i>=n:
    #             return float('inf')
            
    #         state = (i,cur)

    #         if state in dp:
    #             return dp[state]

    #         skip = solve(i+1,cur)

    #         take = 1 + solve(i, cur+coins[i])

    #         dp[state] = min(skip,take)
    #         return dp[state]
        
    #     ans = solve(0,0)

    #     return -1 if ans == float('inf') else ans


    def coinChange(self, coins: list[int], amount: int) -> int:
        
        n = len(coins)
        dp = [[float('inf')]*(amount+1) for _ in range(n+1)]
        
        dp[0][0] = 0

        for i in range(1,n+1):
            coin = coins[i-1]
            for val in range(amount+1):
                skip = dp[i-1][val]

                take = float('inf')
                if val >= coin:
                    take = 1 + dp[i][val - coin]

                dp[i][val] = min(skip,take)
        
        ans = dp[n][amount]
        return -1 if ans == float('inf') else ans