class Solution:
    # def change(self, amount: int, coins: list[int]) -> int:
    #     # dp[i][amount] means:
    #     # Base cell/column:
    #     # Does take read the previous row or current row?
    #     # Row direction:
    #     # Amount direction:
    #     # Final return cell:
        
    #     n = len(coins)
    #     def solve(i,cur):
    #         if cur > amount:
    #             return 0

    #         if cur == amount:
    #             return 1
            
    #         if i>=n:
    #             return 0
            
    #         skip = solve(i+1,cur)

    #         take = solve(i,cur + coins[i])

    #         return take + skip
        
    #     return solve(0,0)
    

    # def change(self, amount: int, coins: list[int]) -> int:
    #     # dp[i][amount] means:
    #     # Base cell/column:
    #     # Does take read the previous row or current row?
    #     # Row direction:
    #     # Amount direction:
    #     # Final return cell:
        
    #     n = len(coins)
    #     dp = {}
    #     def solve(i,cur):
    #         if cur > amount:
    #             return 0

    #         if cur == amount:
    #             return 1
            
    #         if i>=n:
    #             return 0

    #         state = (i,cur)

    #         if state in dp:
    #             return dp[state]
            
    #         skip = solve(i+1,cur)

    #         take = solve(i,cur + coins[i])

    #         dp[state] = take + skip
    #         return dp[state]
        
    #     return solve(0,0)
    

    # def change(self, amount: int, coins: list[int]) -> int:
    #     # dp[i][amount] means: nums of ways to achieve target if coins[i] if added to amount
    #     # Base cell/column: dp[i][target] = 1
    #     # Does take read the previous row or current row? take reads current row
    #     # Row direction: bottom to top
    #     # Amount direction: right to left
    #     # Final return cell: dp[0][0]
        
    #     n = len(coins)
    #     dp = [[0]*(amount + 1) for _ in range(n+1)]

    #     for i in range(n+1):
    #         dp[i][amount] = 1

    #     for i in range(n-1,-1,-1):
    #         for val in range(amount-1,-1,-1):
    #             skip = dp[i+1][val]

    #             take = 0
    #             if val + coins[i] <= amount:
    #                 take = dp[i][val + coins[i]]

    #             dp[i][val] = skip + take
        
    #     return dp[0][0]

    def change(self, amount: int, coins: list[int]) -> int:
        # dp[i][amount] means: nums of ways to achieve target if coins[i] if added to amount
        # Base cell/column: dp[i][target] = 1
        # Does take read the previous row or current row? take reads current row
        # Row direction: bottom to top
        # Amount direction: right to left
        # Final return cell: dp[0][0]
        
        n = len(coins)
        dp = [0]*(amount + 1)

        dp[amount] = 1

        for i in range(n-1,-1,-1):
            for val in range(amount-1,-1,-1):
                skip = dp[val]

                take = 0
                if val + coins[i] <= amount:
                    take = dp[val + coins[i]]

                dp[val] = skip + take
        
        return dp[0]