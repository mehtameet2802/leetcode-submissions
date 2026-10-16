class Solution:
    # def maxProfit(self, prices: list[int], fee: int) -> int:
    #     # common - we do not sell or buy just move on to next day with same hold state
    #     # holding - we sell and move on to next day so we also pay the fee
    #     # not holding - we buy and move on to next day
        
    #     n = len(prices)
    #     def solve(day, holding):

    #         if day >= n:
    #             return 0
            
    #         skip = solve(day+1,holding)

    #         if holding:
    #             action = solve(day+1, False) + prices[day] - fee
    #         else:
    #             action = solve(day+1, True) - prices[day]
        
    #         return max(skip, action)
    
    #     return solve(0, False)


    # def maxProfit(self, prices: list[int], fee: int) -> int:
    #     # common - we do not sell or buy just move on to next day with same hold state
    #     # holding - we sell and move on to next day so we also pay the fee
    #     # not holding - we buy and move on to next day
        
    #     n = len(prices)
    #     dp = {}
    #     def solve(day, holding):

    #         if day >= n:
    #             return 0
            
    #         state = (day,holding)
    #         if state in dp:
    #             return dp[state]
            
    #         skip = solve(day+1,holding)

    #         if holding:
    #             action = solve(day+1, False) + prices[day] - fee
    #         else:
    #             action = solve(day+1, True) - prices[day]

    #         dp[state] = max(skip, action)
    #         return dp[state]
    
    #     return solve(0, False)

    # def maxProfit(self, prices: list[int], fee: int) -> int:
    #     # common - we do not sell or buy just move on to next day with same hold state
    #     # holding - we sell and move on to next day so we also pay the fee
    #     # not holding - we buy and move on to next day
        
    #     n = len(prices)
    #     dp = [[0]*2 for _ in range(n+1)]

    #     for day in range(n-1,-1,-1):
    #         dp[day][0] = max(dp[day+1][0], dp[day+1][1] - prices[day])
    #         dp[day][1] = max(dp[day+1][1], dp[day+1][0] + prices[day] - fee)

    #     return dp[0][0]

    def maxProfit(self, prices: list[int], fee: int) -> int:
        # common - we do not sell or buy just move on to next day with same hold state
        # holding - we sell and move on to next day so we also pay the fee
        # not holding - we buy and move on to next day
        
        n = len(prices)
        dp = [0]*2

        for day in range(n-1,-1,-1):
            dp[0], dp[1] = max(dp[0], dp[1] - prices[day]), max(dp[1], dp[0] + prices[day] - fee)

        return dp[0]